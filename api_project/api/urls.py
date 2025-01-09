from django.urls import path, include  # Include the include function
from rest_framework.routers import DefaultRouter  # Import DefaultRouter
from .views import BookViewSet, BookList  # Import BookViewSet and BookList

# Initialize the DefaultRouter
router = DefaultRouter()

# Register the BookViewSet with the router
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),  # Route for the BookList view
    path('', include(router.urls)),  # Include the router-generated routes
]
