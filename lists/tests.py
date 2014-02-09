from django.core.urlresolvers import resolve
from django.test import TestCase
from lists.views import list_page

class ListPageTest(TestCase):

    def test_list_page_url_resolves_to_list_page_view(self):
        found = resolve('/list/')
        self.assertEqual(found.func, list_page)
