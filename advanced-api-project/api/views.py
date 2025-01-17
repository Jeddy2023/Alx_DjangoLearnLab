from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

class CreateView(generics.CreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]  # Only authenticated users can create books
    """
    View to create a new book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class UpdateView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]  # Only authenticated users can update books
    """
    View to update an existing book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class DeleteView(generics.DestroyAPIView):
    """
    View to delete a specific book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can delete books

class BookListView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]  # Only authenticated users can create books
    """
    View to list all books or create a new book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    View to retrieve, update, or delete a single book by ID.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can update or delete
