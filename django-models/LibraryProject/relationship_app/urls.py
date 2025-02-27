from django.urls import path
from .views import list_books, LibraryDetailView
import relationship_app.views as views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path("books/", list_books, name="list_books"),
    path('book/add_book/', views.add_book, name='add_book'),
    path('book/edit_book/', views.edit_book, name='edit_book'),
    path('book/delete/<int:book_id>/', views.delete_book, name='delete_book'), 
    path("library/<int:pk>/", LibraryDetailView.as_view(), name="library_detail"), 

     path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),

    # Logout view with a custom template
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),

    # Registration view
    path('register/', views.register, name='register'),

    path('admin/', views.admin_view, name='admin_view'), 
    path('librarian/', views.librarian_view, name='librarian_view'), 
    path('member/', views.member_view, name='member_view'),
]