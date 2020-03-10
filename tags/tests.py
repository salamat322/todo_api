from django.urls import reverse

from rest_framework.test import APITestCase
from rest_framework import status

from .models import  Tag



class TestTagAPI(APITestCase):
    def setUp(self):
        Tag.objects.create(name='restAPI')


    def test_get_tags(self):
        """test for get tags"""
        url = reverse('tags-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_tag(self):
        """test for create tag"""
        url = reverse('tag-create')
        tag = {'name': 'rest', 'tasks': [1]}
        response = self.client.post(url, tag, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_tag_detail(self):
        """test for get tag detail"""
        tag = Tag.objects.get(name='restAPI')
        url = tag.get_absolute_url()
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
