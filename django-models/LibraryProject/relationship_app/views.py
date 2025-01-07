from django.shortcuts import render, redirect
from .models import Book
from django.views.generic.detail import DetailView
from .models import Library
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import user_passes_test

def list_books(request):
    books = Book.objects.all() 
    return render(request, "relationship_app/list_books.html", {"books": books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"

class CustomLoginView(LoginView):
    template_name = 'relationship_app/login.html'

class CustomLogoutView(LogoutView):
    template_name = 'relationship_app/logout.html'

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

def is_admin(user):
    return user.userprofile.role == 'Admin'

# Function to check if the user is a Librarian
def is_librarian(user):
    return user.userprofile.role == 'Librarian'

# Function to check if the user is a Member
def is_member(user):
    return user.userprofile.role == 'Member'

# Admin view, accessible only by users with the 'Admin' role
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

# Librarian view, accessible only by users with the 'Librarian' role
@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

# Member view, accessible only by users with the 'Member' role
@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')