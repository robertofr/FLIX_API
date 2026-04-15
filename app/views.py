from django.conf import settings
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect
from django.urls import reverse
from django.utils import translation


def admin_set_language(request: HttpRequest, language_code: str) -> HttpResponse:
    """Switch admin language and return user to the previous page."""
    supported_languages = {code for code, _ in settings.LANGUAGES}
    selected_language = language_code if language_code in supported_languages else settings.LANGUAGE_CODE

    translation.activate(selected_language)

    next_url = request.GET.get('next') or request.META.get('HTTP_REFERER') or reverse('admin:index')
    response = redirect(next_url)
    response.set_cookie(settings.LANGUAGE_COOKIE_NAME, selected_language)
    return response
