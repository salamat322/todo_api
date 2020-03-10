from django.urls import reverse

from rest_framework.test import APITestCase
from rest_framework import status

from .models import Task, Tag


class TestTaskAPI(APITestCase):
    def setUp(self):
        Task.objects.create(name='python', description='test')

    def test_get_tasks(self):
        """test for get tasks list"""
        url = reverse('tasks')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_tasks(self):
        """test for create task"""
        url = reverse('task-create')
        task = {
            'name': "python33",
            'description': 'APItest'
        }
        response = self.client.post(url, task, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    def test_retrieve_task(self):
        """test for retrieve task"""
        task = Task.objects.get(id=1)
        url = task.get_absolute_url()
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


