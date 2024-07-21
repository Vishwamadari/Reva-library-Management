from django.test import TestCase
from django.urls import reverse
from .models import Book

class BookListViewTest(TestCase):
    def test_book_list_view(self):
        # Create some test books
        Book.objects.create(title='Book 1', author='Author 1')
        Book.objects.create(title='Book 2', author='Author 2')

        # Make a GET request to the book list view
        response = self.client.get(reverse('book-list'))

        # Check that the response has a status code of 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check that the response contains the books
        self.assertContains(response, 'Book 1')
        self.assertContains(response, 'Book 2')

        # Check that the response uses the correct template
        self.assertTemplateUsed(response, 'viewbook.html')