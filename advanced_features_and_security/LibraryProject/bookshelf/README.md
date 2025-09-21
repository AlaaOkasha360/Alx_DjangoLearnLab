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

# Security Measures Implemented

## Settings (`settings.py`)
- `DEBUG = False` → prevents sensitive debug info in production.
- `SECURE_BROWSER_XSS_FILTER = True` → enables XSS filter in browsers.
- `X_FRAME_OPTIONS = "DENY"` → prevents clickjacking.
- `SECURE_CONTENT_TYPE_NOSNIFF = True` → stops MIME-type sniffing.
- `CSRF_COOKIE_SECURE = True` & `SESSION_COOKIE_SECURE = True` → cookies only over HTTPS.
- CSP (Content Security Policy) → restricts resources to same-origin.

## Templates
- `{% csrf_token %}` added to all forms.
- `|escape` filter applied to user-generated content to prevent XSS.

## Views
- Used Django ORM instead of raw SQL → prevents SQL injection.
- Input validation done via Django `forms.py`.

## Testing
1. Verified CSRF tokens appear in forms.
2. Tested invalid user input → safely handled without breaking queries.
3. Inspected responses → CSP headers present.
