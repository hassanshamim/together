from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest

from lists.views import list_page


class ListPageTest(TestCase):

    def test_list_page_url_resolves_to_list_page_view(self):
        found = resolve('/list/')
        self.assertEqual(found.func, list_page)

    def test_list_page_returns_correct_html(self):
        request = HttpRequest()
        response = list_page(request)
        self.assertTrue(response.content.startswith(b'<html>'))
        self.assertIn(b'<title>To-Do lists</title>', response.content)
        self.assertTrue(response.content.endswith(b'</html>'))

    def user_creates_list(self):
        # As a logged in user Joan...
        # I create a To-Do list 'Gifts'
        # I add 'Grab bag gift' as a todo item
        # I describe it as "Less then $5, wrapped, to be exchanged after dinner before dessert"



