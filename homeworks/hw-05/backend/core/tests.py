from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework import status
from .models import Post, Comment

class BlogTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.client.force_authenticate(user=self.user)
        self.post = Post.objects.create(title='Test Post', content='Content', author=self.user)

    def test_create_post(self):
        url = '/api/posts/'
        data = {'title': 'New Post', 'content': 'New Content'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_posts(self):
        url = '/api/posts/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_comment(self):
        url = '/api/comments/'
        data = {'post': self.post.id, 'content': 'Test Comment'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_unauthenticated_post_fail(self):
        self.client.force_authenticate(user=None)
        url = '/api/posts/'
        data = {'title': 'Fail', 'content': 'Fail'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
