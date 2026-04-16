from django.contrib import admin
from django.urls import path, include
from app.views import admin_set_language

urlpatterns = [
    path('admin/lang/pt-br/', admin_set_language, {'language_code': 'pt-br'}, name='admin-language-ptbr'),
    path('admin/lang/en/', admin_set_language, {'language_code': 'en'}, name='admin-language-en'),
    path('admin/', admin.site.urls),

    #Authentication
    path('api/v1/', include('authentication.urls')),
    #Genres
    path('api/v1/', include('genres.urls')),
    #Actors
    path('api/v1/', include('actors.urls')),
    #Movies
    path('api/v1/', include('movies.urls')),
    #Reviews
    path('api/v1/', include('reviews.urls')),
]
