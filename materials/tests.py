from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from materials.models import Course, Lesson
from users.models import User, SubscriptionForUpdate


class LessonTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email='fortest@mail.com')
        self.course = Course.objects.create(title_course='Test Course', description='Test Description', owner=self.user)
        self.lesson = Lesson.objects.create(
            title_lesson='Test Lesson', description='Test description', course=self.course,
            link_to_video='https://www.youtube.com/watch?v=abc123', owner=self.user
        )
        self.client.force_authenticate(user=self.user)

    def test_lesson_retrieve(self):
        url = reverse('materials:lesson_detail', args=(self.lesson.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data.get('title_lesson'), self.lesson.title_lesson
        )

    def test_lesson_create(self):
        url = reverse('materials:lesson_create')
        data = {
            'title_lesson': 'Test Create',
            'description': 'Test Create Lesson',
            'link_to_video': 'https://www.youtube.com/'
        }
        response = self.client.post(url, data)
        self.assertEqual(
            response.status_code, status.HTTP_201_CREATED
        )

    def test_lesson_list(self):
        url = reverse('materials:lesson_list')
        response = self.client.get(url)
        data = response.json()
        result = {
            'count': 1,
                  'next': None,
                  'previous': None,
                  'results': [
                      {
                          'id': self.lesson.pk,
                          'title_lesson': self.lesson.title_lesson,
                          'preview': None,
                          'description': self.lesson.description,
                          'link_to_video': self.lesson.link_to_video,
                          'course': self.course.pk,
                          'owner': self.user.pk
                      }
                  ]
        }
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data, result
        )

    def test_lesson_update(self):
        url = reverse('materials:lesson_update', args=(self.lesson.pk,))
        data = {
            'title_lesson': 'Test Lesson Update',
            'description': 'Test Create Lesson',
            'link_to_video': 'https://www.youtube.com/'
        }
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data.get('title_lesson'), 'Test Lesson Update'
        )

    def test_lesson_delete(self):
        url = reverse('materials:lesson_delete', args=(self.lesson.pk,))
        response = self.client.delete(url)
        self.assertEqual(
            response.status_code, status.HTTP_204_NO_CONTENT
        )
        self.assertEqual(
            Lesson.objects.all().count(), 0
        )


class SubscriptionTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email='fortest@mail.com')
        self.course = Course.objects.create(title_course='Test Course', description='Test Description', owner=self.user)
        self.client.force_authenticate(user=self.user)

    def test_subscribe(self):
        url = reverse('users:subscription')
        data = {
            'course': self.course.pk
        }
        response = self.client.post(url, data)
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            response.json(), {"message": "Подписка добавлена"}
        )

    def test_unsubscribe(self):
        self.subscription = SubscriptionForUpdate.objects.create(user=self.user, course=self.course)
        url = reverse('users:subscription')
        data = {
            'course': self.course.pk
        }
        response = self.client.post(url, data)
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            response.json(), {"message": "Подписка удалена"}
        )
