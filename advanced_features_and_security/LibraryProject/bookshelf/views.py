from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .models import Document
from bookshelf.models import Book

def book_list(request):
    query = request.GET.get('q', '')
    if query:
        # Validate user input
        books = Book.objects.filter(title__icontains=query)
    else:
        books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

@permission_required('bookshelf.can_view', raise_exception=True)
def document_list(request):
    documents = Document.objects.all()
    return render(request, 'bookshelf/document_list.html', {'documents': documents})

@permission_required('bookshelf.can_create', raise_exception=True)
def document_create(request):
    if request.method == 'POST':
        # Handle form submission
        pass
    return render(request, 'bookshelf/document_form.html')

@permission_required('bookshelf.can_edit', raise_exception=True)
def document_edit(request, pk):
    document = get_object_or_404(Document, pk=pk)
    if request.method == 'POST':
        # Handle form submission
        pass
    return render(request, 'bookshelf/document_form.html', {'document': document})

@permission_required('bookshelf.can_delete', raise_exception=True)
def document_delete(request, pk):
    document = get_object_or_404(Document, pk=pk)
    document.delete()
    return redirect('book_list')
