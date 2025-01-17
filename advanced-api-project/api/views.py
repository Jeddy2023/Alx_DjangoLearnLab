class BookListView(generics.ListCreateAPIView):
    """
    Handles the listing of all books and the creation of a new book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [AllowAny]

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Handles the retrieval, updating, and deletion of a specific book by ID.
    Only authenticated users can update or delete books.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
