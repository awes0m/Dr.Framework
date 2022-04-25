from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful
        """
        email = 'tester@apisod.com'
        password = 'test123'
        user = get_user_model().\
            objects.create_user(email=email, password=password)

        self.assertEqual(user.email, email)
        # return True if the password is correct
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """_summary_: Test the email for a new user is normalized"""
        email = 'tester@apisod.com'
        user = get_user_model().objects.create_user(email, 'test123')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """_summary_: Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_create_new_superuser(self):
        """_summary_: Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            'tester@apisod.com',
            'test123'
        )

        self.assertTrue(expr=user.is_superuser)
        self.assertTrue(expr=user.is_staff)
