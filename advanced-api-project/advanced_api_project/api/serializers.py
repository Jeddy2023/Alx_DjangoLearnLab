from rest_framework import serializers
from .models import Author, Book
import datetime

"""
This module defines serializers for the API.

Serializers:
- BookSerializer: Serializes the Book model with custom validation for publication_year.
- AuthorSerializer: Serializes the Author model and includes nested BookSerializer for related books.
"""

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    def validate_publication_year(self, value):
        """Ensure the publication year is not in the future."""
        current_year = datetime.datetime.now().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name', 'books']
