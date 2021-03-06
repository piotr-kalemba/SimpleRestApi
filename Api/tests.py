from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from .models import Book


class TestHomeView(APITestCase):

    def setUp(self):
        Book.objects.create(title='title_1', author='author_1', isbn='978-1-16-148410-0')
        Book.objects.create(title='title_2', author='author_2', isbn='978-2-16-148410-0')

    def test_get(self):
        url = reverse('home')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_post(self):
        url = reverse('home')
        data = {'title': 'The Trial', 'author': 'Franz Kafka', 'isbn': '978-3-16-148410-0'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(Book.objects.count(), 3)
        self.assertEqual(response.data['title'], data['title'])
        self.assertEqual(response.data['author'], data['author'])
        self.assertEqual(response.data['isbn'], data['isbn'])


class TestBookView(APITestCase):

    def setUp(self):
        Book.objects.create(title='Mock Title', author='Mock Author', isbn='000-0-00-000000-0')
        book = Book.objects.create(title='The Name of the Rose', author='Umberto Eco', isbn='978-5-16-148410-0')
        book.save()
        self.id = book.id

    def test_get(self):
        url = reverse('book', args=(self.id, ))
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'The Name of the Rose')
        self.assertEqual(response.data['author'], 'Umberto Eco')
        self.assertEqual(response.data['isbn'], '978-5-16-148410-0')

    def test_delete(self):
        count_before = Book.objects.count()
        url = reverse('book', args=(self.id,))
        response = self.client.delete(url)
        count_after = Book.objects.count()
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(count_before, count_after + 1)






