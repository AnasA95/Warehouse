from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from whss.models import User as U

User = get_user_model()


class UserAPITestCase(APITestCase):
    def setUp(self):
        user = User.objects.create(username='test', email='test@test.com')
        user.set_password('a')
        user.save()

    def test_single_user(self):
        user_count = User.objects.count()
        self.assertEqual(user_count, 1)

    def test_single_u(self):
        u_count = U.objects.count()
        self.assertEqual(u_count, 1)

