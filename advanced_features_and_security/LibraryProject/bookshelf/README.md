# Managing Permissions and Groups

## Custom Permissions
- `can_view`: Can view documents
- `can_create`: Can create documents
- `can_edit`: Can edit documents
- `can_delete`: Can delete documents

## User Groups
1. **Viewers**: Assigned `can_view`.
2. **Editors**: Assigned `can_view`, `can_create`, `can_edit`.
3. **Admins**: Assigned all permissions.

## Testing
- Assign users to groups in the admin panel.
- Verify access by logging in with users in different groups.
