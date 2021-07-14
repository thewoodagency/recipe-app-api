from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """test creating a new user with email"""
        email = "test@test.com"
        password = "123456"

        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """test email for a new user is normalized"""
        email = 'test@TEST.com'
        user = get_user_model().objects.create_user(email, 'password')
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """test creating user wiht no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('', 'testp')

    def test_create_new_superuser(self):
        """test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            'admin@test.com',
            'password'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
