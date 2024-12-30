from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from .models import Book, BorrowedBook
from .forms import BookEntryForm, UserInfoForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
import random 
import json
import csv  # Import CSV module
from django.conf import settings
from datetime import datetime
import os  # Import os module to handle file paths

def home(request):
    return render(request, 'home.html') 

def borrow_book(request):
    # Get all books with available copies
    books = Book.objects.filter(available_copies__gt=0).values(
        'id', 'title', 'author', 'category', 'published_year', 'description'
    )

    if request.method == "POST":
        # Extract selected book ID from form data
        book_id = request.POST['book_id']
        return redirect(reverse('user_info', args=[book_id]))
    
    # Serialize book data for JavaScript
    books_json = json.dumps(list(books))
    return render(request, 'borrow.html', {'books': books_json})

def user_info(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    
    if request.method == "POST":
        form = UserInfoForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            
            # Generate a unique borrow code
            borrow_code = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=8))
            
            # Create a BorrowedBook record
            borrowed_book = BorrowedBook(
                book=book, 
                borrow_code=borrow_code, 
                date_due="2024-01-15",  # Example due date
                email=email,
                phone=phone
            )
            borrowed_book.save()
            
            # Update the book's available copies
            book.available_copies -= 1
            book.save()
            
            # Export details to CSV file
            csv_file_path = os.path.join(settings.BASE_DIR, 'borrowed_books.csv')
            with open(csv_file_path, mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([book.title, email, datetime.now().strftime("%Y-%m-%d"), borrow_code])
            
            # Render a template instead of passing JavaScript through HttpResponse
            return render(request, 'borrow_success.html', {'borrow_code': borrow_code, 'book_title': book.title})
    else:
        form = UserInfoForm()
    
    return render(request, 'user_info.html', {'form': form, 'book': book})

def return_book(request):
    if request.method == "POST":
        # Extract borrow code from form data
        borrow_code = request.POST['borrow_code']
        
        # Find the corresponding BorrowedBook record
        borrowed_book = BorrowedBook.objects.filter(borrow_code=borrow_code).first()
        
        if borrowed_book:
            # Increment available copies of the book
            book = borrowed_book.book
            book.available_copies += 1
            book.save()
            
            # Delete the BorrowedBook record
            borrowed_book.delete()
            
            return render(request, 'return_success.html', {'book_title': book.title})
        
        return HttpResponse("<h1 class='flex justify-center align-center text-center'>Invalid borrow code.</h1>")
    
    return render(request, 'return.html')

@login_required
def book_entry(request):
    # Restrict access to the librarian only
    if not request.user.is_staff or request.user.username != 'librarian':
        messages.error(request, 'Access denied. Only the librarian can access this page.')
        return redirect('home')  # Redirect unauthorized users to the home page

    if request.method == 'POST':
        # Verify the entered password:
            form = BookEntryForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()  # Save the book to the database
                messages.success(request, 'Book added successfully!')
                return redirect('book_entry')  # Redirect to clear the form after successful entry
            else:
                messages.error(request, 'Invalid form submission. Please correct the errors below.')
    else:
        # Provide an empty form for GET requests
        form = BookEntryForm()

    return render(request, 'book_entry.html', {'form': form})

def search_books(request):
    query = request.GET.get('q', '')
    books = Book.objects.filter(name__icontains=query)
    results = [{'name': book.name} for book in books]
    return JsonResponse({'books': results})