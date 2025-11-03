"""
Docker-specific settings for haga project.
"""

import os
from .settings import *

# Override settings for Docker environment
DEBUG = os.getenv('DEBUG', 'False').lower() == 'true'

ALLOWED_HOSTS = ['*']  # In production, specify your domain

# Database configuration for PostgreSQL (when using docker-compose)
if os.getenv('USE_POSTGRES', 'False').lower() == 'true':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.getenv('POSTGRES_DB', 'haga_db'),
            'USER': os.getenv('POSTGRES_USER', 'haga_user'),
            'PASSWORD': os.getenv('POSTGRES_PASSWORD', 'haga_password'),
            'HOST': os.getenv('DB_HOST', 'db'),
            'PORT': os.getenv('DB_PORT', '5432'),
        }
    }

# Static files configuration
STATIC_ROOT = '/app/staticfiles'

# Security settings (uncomment for production)
# SECURE_BROWSER_XSS_FILTER = True
# SECURE_CONTENT_TYPE_NOSNIFF = True
# X_FRAME_OPTIONS = 'DENY'
