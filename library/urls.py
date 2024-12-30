from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('borrow/', views.borrow_book, name='borrow'),
    path('user_info/<int:book_id>/', views.user_info, name='user_info'),
    path('return/', views.return_book, name='return'),
    path('book-entry/', views.book_entry, name='book_entry'),
    path('search_books/', views.search_books, name='search_books'),
]