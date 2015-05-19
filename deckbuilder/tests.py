from django.template.loader import render_to_string
from django.core.urlresolvers import resolve
from django.test import TestCase

from deckbuilder.views import home

class HomePageTest(TestCase):

    def test_root_utl_resolves_to_home_view(self):
        response = resolve('/')
        self.assertEqual(response.func, home)

    def home_page_returns_the_correct_html(self):
        request = HttpRequest()
        response = home(request)
        expected = render_to_string('home.html')
        self.assertEqual(response.content.decode(), expected)
