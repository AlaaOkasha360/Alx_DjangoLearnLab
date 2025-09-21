# Permissions and Groups Setup

## Custom Permissions
Defined in `Book` model (`models.py`):
- can_view
- can_create
- can_edit
- can_delete

## Groups
Set up via Django Admin:
- **Viewers** → assign `can_view`
- **Editors** → assign `can_view`, `can_create`, `can_edit`
- **Admins** → assign all (`can_view`, `can_create`, `can_edit`, `can_delete`)

## Enforcing Permissions
Views in `views.py` use `@permission_required`:
- `book_list` → requires `can_view`
- `book_create` → requires `can_create`
- `book_edit` → requires `can_edit`
- `book_delete` → requires `can_delete`

## Testing
1. Create test users.
2. Assign them to groups in the Admin.
3. Log in and try accessing book views.
   - Users without the required permission will get a 403 error.
