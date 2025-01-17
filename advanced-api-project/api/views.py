from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters import rest_framework
from rest_framework import filters

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
    """
    View to list all books or create a new book.
    Supports filtering, searching, and ordering.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Allows unauthenticated users to read the list of books

    # Enable filtering, searching, and ordering
    filter_backends = (rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filterset_fields = ['title', 'author', 'publication_year']  # Allow filtering by title, author, and publication_year
    search_fields = ['title', 'author__name']  # Enable search on book title and author name
    ordering_fields = ['title', 'publication_year']  # Allow ordering by title or publication year
    ordering = ['title']

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    View to retrieve, update, or delete a single book by ID.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can update or delete
