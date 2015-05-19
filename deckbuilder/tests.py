from django.http import HttpRequest
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
        expected_html = render_to_string('home.html')
        self.assertEqual(response.content.decode(), expected_html)

    def test_home_page_can_save_a_POST_request(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['deck_text'] = 'A new deck item'

        response = home(request)
        self.assertIn('A new deck item', response.content.decode())
        expected = render_to_string(
            'home.html',
            {'new_deck_text': 'A new deck item'}
        )
        self.assertEqual(response.content.decode(), expected)
