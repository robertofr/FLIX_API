from pathlib import Path
from datetime import timedelta
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/6.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-lfw^hn#01cqdxz^_p27xk2y9dr&r+94nzdykt!lc0p4y270lb)'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'unfold',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'rest_framework_simplejwt',

    'genres',
    'actors',
    'movies',
    'reviews',
    'authentication',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'app.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'app.wsgi.application'


# Database
# https://docs.djangoproject.com/en/6.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/6.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/6.0/topics/i18n/

LANGUAGE_CODE = 'pt-br'

LANGUAGES = [
    ('pt-br', _('Portugues (Brasil)')),
    ('en', _('English')),
]

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/6.0/howto/static-files/

STATIC_URL = 'static/'


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=500),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=2),
}


UNFOLD = {
    'SITE_TITLE': 'Flix API Admin',
    'SITE_HEADER': 'Flix API',
    'SITE_SUBHEADER': 'Painel administrativo',
    'SITE_URL': '/',
    'SITE_SYMBOL': 'movie',
    'SITE_DROPDOWN': [
        {
            'icon': 'home',
            'title': 'Voltar para o Admin',
            'link': reverse_lazy('admin:index'),
        },
        {
            'icon': 'language',
            'title': 'Idioma: Portugues',
            'link': reverse_lazy('admin-language-ptbr'),
        },
        {
            'icon': 'language',
            'title': 'Language: English',
            'link': reverse_lazy('admin-language-en'),
        },
    ],
    'SHOW_HISTORY': True,
    'SHOW_VIEW_ON_SITE': True,
    'SHOW_BACK_BUTTON': False,
    'BORDER_RADIUS': '8px',
    'SIDEBAR': {
        'show_search': True,
        'command_search': True,
        'show_all_applications': False,
        'navigation': [
            {
                'title': 'Navegacao',
                'separator': True,
                'collapsible': False,
                'items': [
                    {
                        'title': 'Dashboard',
                        'icon': 'dashboard',
                        'link': reverse_lazy('admin:index'),
                    },
                ],
            },
            {
                'title': 'Catalogo',
                'separator': True,
                'collapsible': True,
                'items': [
                    {
                        'title': 'Filmes',
                        'icon': 'theaters',
                        'link': reverse_lazy('admin:movies_movies_changelist'),
                    },
                    {
                        'title': 'Generos',
                        'icon': 'category',
                        'link': reverse_lazy('admin:genres_genre_changelist'),
                    },
                    {
                        'title': 'Atores',
                        'icon': 'groups',
                        'link': reverse_lazy('admin:actors_actor_changelist'),
                    },
                    {
                        'title': 'Reviews',
                        'icon': 'reviews',
                        'link': reverse_lazy('admin:reviews_review_changelist'),
                    },
                ],
            },
            {
                'title': 'Seguranca',
                'separator': True,
                'collapsible': True,
                'items': [
                    {
                        'title': 'Usuarios',
                        'icon': 'person',
                        'link': reverse_lazy('admin:auth_user_changelist'),
                    },
                    {
                        'title': 'Grupos',
                        'icon': 'shield',
                        'link': reverse_lazy('admin:auth_group_changelist'),
                    },
                ],
            },
        ],
    },
}