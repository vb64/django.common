# -*- coding: utf-8 -*-

from django.utils import translation
from emoji import Country

COOKIE_NAME = 'lang'
DEFAULT_CODE = 'en'

LANGUAGES = {
    'en': 'English',
    'ru': 'Русский',
}

FLAGS = {
    'en': Country.UnitedKingdom,
    'ru': Country.Russia,
}

languages = [x for x in LANGUAGES.keys() if x != 'en']


def flag_text(lang):
    return FLAGS.get(lang, '') + u' ' + LANGUAGES.get(lang, '')


def fake_gettext(text):
    return text


def get_lang(code):
    if not code:
        return ''
    for l in languages:
        if l in code:
            return l
    return ''


def lang_for_user(from_user):
    lang = get_lang(from_user.language_code)
    if lang:
        activate(lang)


def activate(lang):
    old = translation.get_language()
    translation.activate(lang)
    return old


def ua_languages(http_accept_language, lang_list, lang_dflt):
    lst = []
    for itm in http_accept_language.split(','):
        if ';' in itm:
            itm = itm.split(';')[0]
        if '-' in itm:
            itm = itm.split('-')[0]
        if itm not in lst:
            lst.append(itm)

    for lng in lst:
        if lng in lang_list:
            return lng

    return lang_dflt


class Context():
    code = DEFAULT_CODE

    def process_request(self, request):

        if COOKIE_NAME in request.COOKIES.keys():
            new_code = request.COOKIES[COOKIE_NAME]
            if new_code in LANGUAGES.keys():
                self.code = new_code
        else:
            self.code = ua_languages(
              request.META.get('HTTP_ACCEPT_LANGUAGE', ''),
              LANGUAGES.keys(),
              DEFAULT_CODE
            )

        activate(self.code)
        return None


def template_context(request):
    return {
      'lang': translation.get_language(),
      'lang_list': LANGUAGES,
    }
