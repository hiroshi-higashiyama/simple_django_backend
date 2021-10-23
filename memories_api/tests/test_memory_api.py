from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth import get_user_model
from memories_api import models, serializers


LIST_URL_MEMEORY_API = reverse('memory-list')


class PublicUnitTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_login_access(self):
        res = self.client.get(LIST_URL_MEMEORY_API)
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivateUnitTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            'fake@studyeasy.org',
            'password123'
        )
        self.client.force_authenticate(self.user)

    def test_list_memories(self):
        models.Tag.objects.create(tag='new Tag')
        tag = models.Tag.objects.get(pk=1)
        memory = models.Memory.objects.create(
            title='title',
            description='description',
            owner=self.user,
            date=timezone.now()
        )
        memory.tags.add(tag)

        res = self.client.get(LIST_URL_MEMEORY_API)
        memories = models.Memory.objects.all()
        serializer = serializers.MemorySerializer(memories, many=True)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

