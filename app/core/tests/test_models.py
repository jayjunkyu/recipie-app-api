from django.test import TestCase
from django.contrib.auth import get_user_model


TEST_EMAIL = 'test@gmail.com'
TEST_PASSWORD = 'testpassword'


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful"""
        user = get_user_model().objects.create_user(
            email=TEST_EMAIL,
            password=TEST_PASSWORD
        )

        self.assertEqual(user.email, TEST_EMAIL)
        self.assertTrue(user.check_password(TEST_PASSWORD))

    def test_new_user_email_normalize(self):
        """Test the email for a new user is normalized"""
        unnormalized_email = 'test@GMAIL.COM'
        user = get_user_model().objects.create_user(
            unnormalized_email, TEST_PASSWORD
        )

        self.assertEqual(user.email, unnormalized_email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
                email=None, password=TEST_PASSWORD
            )

    def test_create_new_superuser(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            email=TEST_EMAIL,
            password=TEST_PASSWORD
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
