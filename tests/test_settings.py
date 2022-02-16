import os

INSTALLED_APPS = (
    'tests.test_app',
)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "tests.sqlite3"),
    }
}
SECRET_KEY = 'dummy'

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}

USE_TZ = False
