from rest_framework import viewsets
from .models import Book  # Import the Book model
from .serializers import BookSerializer  # Import the BookSerializer
from rest_framework import permissions
from .permissions import IsAdminOrReadOnly

class BookViewSet(viewsets.ModelViewSet):  # Extend ModelViewSet
    queryset = Book.objects.all()  # QuerySet for the Book model
    serializer_class = BookSerializer  # Serializer for the Book model
    permission_classes = [permissions.IsAuthenticated, IsAdminOrReadOnly]