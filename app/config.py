"""App development configuration."""

import pathlib

# Root of this application, useful if it doesn't occupy an entire domain
APPLICATION_ROOT = '/'

# Secret key for encrypting cookies
SECRET_KEY = b'\xb6k\x078\x0c6RB\x15-\x8a\x01\xd9Y\x00\xf5\xc0Lw=\xb5\xc3\x02|'
SESSION_COOKIE_NAME = 'login'

# File Upload to var/uploads/
APP_ROOT = pathlib.Path(__file__).resolve().parent.parent
UPLOAD_FOLDER = APP_ROOT/'var'/'uploads'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
MAX_CONTENT_LENGTH = 16 * 1024 * 1024

# Database file is var/app.sql
DATABASE_FILENAME = APP_ROOT/'var'/'app.sql'