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
        self.assertEqual(response.data['title'], 'The Trial')
        self.assertEqual(response.data['author'], 'Franz Kafka')
        self.assertEqual(response.data['isbn'], '978-3-16-148410-0')

