from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSiteTests(TestCase):
    def setUp(self):
        """
        The setUp function is used to create a user
        and log them in before each test.

        It creates and logs in with a super user
        and using taht access then creates and logs in with a normal user.
        This is useful as you don't have to create a new user for every test,
        which saves time.
        :param self: Refer to instance attributes or methods
        :return: A client object that has a logged-in user

        """

        # create a test [Client]-
        # The test client is a Python class that acts as a dummy Web browser,
        # allowing you to test your views and interact with
        # your Django-powered application programmatically.
        self.client = Client()
        # creates an superuser called 'admin_user'
        self.admin_user = get_user_model().objects.create_superuser(
            email='admin@apisod.com',
            password='password123'
        )

        # Login the admin_user(superuser)
        self.client.force_login(self.admin_user)
        # Create a user for testing using the superuser account
        self.user = get_user_model().objects.create_user(
            email='test@apisod.com',
            password='password123',
            name='Test User full name'
        )

    def test_users_listed(self):
        """
        The test_users_listed function tests that users are listed
        on the user page.
        The reverse function is used to get the URL for the list user page,
        (https://docs.djangoproject.com/en/2.1/ref/contrib/admin/#reversing-admin-urls)
        and then we make a GET request to that URL.
        We should expect a response of 200 OK.
        :param self: Reference the class instance
        :return: A response object
        """

        url = reverse('admin:core_user_changelist')
        # get the response from the URL
        res = self.client.get(url)

        # check that the response is 200 OK
        # and that the user and email is listed
        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

    def test_user_change_page(self):
        """
        The test_user_change_page function tests that the user edit page works
        correctly.
        The reverse function is used to get the URL for the edit user page,
        (https://docs.djangoproject.com/en/2.1/ref/contrib/admin/#reversing-admin-urls)
        eg. /admin/core/user/1/change/
        and then we make a GET request to that URL.
        We should expect a response of 200 OK.

        :param self: Reference the class instance
        :return: A response object
        """
        url = reverse('admin:core_user_change', args=[self.user.id])
        # eg. /admin/core/user/[user.id]/change/
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
