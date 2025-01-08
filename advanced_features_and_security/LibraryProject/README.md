### Utilizing the Django Admin Interface

#### Objective
Integrate the `Book` model with the Django admin interface to enhance data management capabilities.

#### Steps Implemented
1. **Registered the Book Model**  
   - Enabled admin functionalities for the `Book` model by modifying `bookshelf/admin.py`.

2. **Customizations in Admin**
   - Displayed `title`, `author`, and `publication_year` in the admin list view using `list_display`.
   - Added search capabilities for `title` and `author` using `search_fields`.
   - Configured a filter for `publication_year` using `list_filter`.

#### Results
- Admin interface now displays relevant fields for books.
- Improved usability with search and filter functionalities.
- Verified changes in the Django admin at [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin).
