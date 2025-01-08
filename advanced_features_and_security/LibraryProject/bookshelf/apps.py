from django.apps import AppConfig
from django.contrib.auth.models import Group, Permission

class BookShelfAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bookshelf'

    def ready(self):
        # Create groups and assign permissions
        Group.objects.get_or_create(name='Editors')
        Group.objects.get_or_create(name='Viewers')
        Group.objects.get_or_create(name='Admins')

        # Assign permissions to groups
        from django.contrib.contenttypes.models import ContentType
        content_type = ContentType.objects.get(app_label='bookshelf', model='document')
        
        # Permissions
        can_view = Permission.objects.get(codename='can_view', content_type=content_type)
        can_create = Permission.objects.get(codename='can_create', content_type=content_type)
        can_edit = Permission.objects.get(codename='can_edit', content_type=content_type)
        can_delete = Permission.objects.get(codename='can_delete', content_type=content_type)

        editors = Group.objects.get(name='Editors')
        editors.permissions.add(can_view, can_create, can_edit)

        viewers = Group.objects.get(name='Viewers')
        viewers.permissions.add(can_view)

        admins = Group.objects.get(name='Admins')
        admins.permissions.add(can_view, can_create, can_edit, can_delete)
