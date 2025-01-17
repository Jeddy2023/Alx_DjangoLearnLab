from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from .models import Book
from rest_framework.permissions import IsAuthenticated
from rest_framework.test import APIClient

class BookAPITests(APITestCase):
    def setUp(self):
        # Create a user for authentication
        self.user = User.objects.create_user(username='testuser', password='password')
        self.client = APIClient()
        self.client.login(username='testuser', password='password')

        # Create some books to test with
        self.book1 = Book.objects.create(title="Book 1", author="Author 1", publication_year=2021)
        self.book2 = Book.objects.create(title="Book 2", author="Author 2", publication_year=2022)

    def test_create_book(self):
        """Test that a book can be created."""
        url = '/api/books/'
        data = {
            'title': 'Book 3',
            'author': 'Author 3',
            'publication_year': 2023,
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)
        self.assertEqual(Book.objects.get(title='Book 3').author, 'Author 3')

    def test_update_book(self):
        """Test that a book can be updated."""
        url = f'/api/books/{self.book1.id}/'
        data = {'title': 'Updated Book 1'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, 'Updated Book 1')

    def test_delete_book(self):
        """Test that a book can be deleted."""
        url = f'/api/books/{self.book1.id}/'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    def test_book_list_view(self):
        """Test that the book list view works and filters correctly."""
        url = '/api/books/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  # There should be 2 books in the DB

    def test_search_books(self):
        """Test that searching books by title works."""
        url = '/api/books/?search=Book 1'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Book 1')

    def test_filter_books_by_author(self):
        """Test that filtering books by author works."""
        url = '/api/books/?author=Author 1'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['author'], 'Author 1')

    def test_order_books_by_publication_year(self):
        """Test that ordering books by publication year works."""
        url = '/api/books/?ordering=publication_year'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], 'Book 1')
        self.assertEqual(response.data[1]['title'], 'Book 2')

    def test_permissions_for_create_update_delete(self):
        """Test that the correct permissions are enforced."""
        # Attempt to create a book without authentication
        self.client.logout()
        url = '/api/books/'
        data = {'title': 'Book 4', 'author': 'Author 4', 'publication_year': 2024}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        # Test creating with authentication
        self.client.login(username='testuser', password='password')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
