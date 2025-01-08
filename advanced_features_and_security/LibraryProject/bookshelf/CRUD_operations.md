# CRUD Operations Documentation

This document contains the steps to perform Create, Retrieve, Update, and Delete (CRUD) operations on the `Book` model in the Django app `bookshelf`.

---

## Create a Book Instance

### Command:
from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
book

#### Output:
<Book: 1984 by George Orwell (1949)>

## Retrieve the Book

### Command:
Book.objects.all()

#### Output:
<QuerySet [<Book: 1984 by George Orwell (1949)>]>


## Update the Book Title

### Command:
book.title = "Nineteen Eighty-Four"
book.save()
book

#### Output:
<Book: Nineteen Eighty-Four by George Orwell (1949)>


## Delete the Book

### Command:
book.delete()
Book.objects.all()

#### Output:
(1, {'bookshelf.Book': 1})
<QuerySet []>