from django.urls import path
from .views import BookListView, BookDetailView, CreateView, UpdateView, DeleteView

urlpatterns = [
    path('books/', BookListView.as_view(), name='book-list'),  # Lists all books or creates a new book
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),  # Retrieves, updates, or deletes a book by ID
    path('books/create/', CreateView.as_view(), name='book-create'),  # Creates a new book
    path('books/update', UpdateView.as_view(), name='book-update'),  # Updates a book
    path('books/delete', DeleteView.as_view(), name='book-delete'),  # Deletes a book
]
