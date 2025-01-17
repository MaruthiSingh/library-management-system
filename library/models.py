from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator
import os
from PIL import Image
import shutil

class Book(models.Model):
    title = models.CharField(max_length=200, verbose_name="Book Title")
    author = models.CharField(max_length=100, verbose_name="Author")
    category = models.CharField(max_length=100, verbose_name="Category")
    published_year = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1000),  # Minimum year
            MaxValueValidator(9999),  # Maximum year
        ]
    )
    available_copies = models.PositiveIntegerField(verbose_name="Available Copies", default=0)
    
    #Validation for isbn Field:
    #Ensure that the isbn field is validated to be exactly 13 characters long.
    isbn = models.CharField(
        max_length=14, unique=True, null=True, verbose_name="ISBN",
        help_text="13-character ISBN number",
        validators=[RegexValidator(regex='^\d{13}$', message='ISBN must be exactly 13 digits')]
    )
    
    description = models.TextField(verbose_name="Description", blank=True, help_text="Optional description or summary of the book")
    cover_image = models.ImageField(upload_to='book_covers/', verbose_name="Book Cover", blank=True, null=True, help_text="Optional cover image for the book")

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.cover_image:
            self.save_cover_image()

    #Fault Tolerance in Image Processing:
    #Add error handling for image processing to avoid crashes if the image file is corrupted or missing.
    #Null Handling for cover_image:
    #Ensure that cover_image is handled properly when it's None.
    def save_cover_image(self):
        try:
            cover_image_path = self.cover_image.path
            new_image_path = f'static/images/cover_images/{self.id}.jpg'
            os.makedirs(os.path.dirname(new_image_path), exist_ok=True)
            with Image.open(cover_image_path) as img:
                img = img.resize((180, 276), Image.LANCZOS)
                img.save(new_image_path)
        except Exception as e:
            print(f"Error processing cover image: {e}")

    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"
        ordering = ['title']

    def __str__(self):
        return f"{self.title} by {self.author}"

    def borrow(self):
        if self.available_copies > 0:
            self.available_copies -= 1
            self.save()
            return True
        return False


class BorrowedBook(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrow_code = models.CharField(max_length=10, unique=True)
    date_borrowed = models.DateField(auto_now_add=True)
    date_due = models.DateField()
    email = models.EmailField(default=None)
    phone = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return f"{self.book.title} - {self.borrow_code}"
