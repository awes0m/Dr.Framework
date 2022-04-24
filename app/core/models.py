from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
    PermissionsMixin


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        """Creates and saves a new user"""
        if not email:
            """If no email is provided, raise an error"""
            raise ValueError('Users must have an email address')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """
        The create_superuser function creates a new super user
        by calling the create_user function from above.
        The extra values being attached to
        make superuser is passed through
        the is_staff and is_superuser variables.
        This will then save it in the database.

        :param self: Reference the current instance of the class
        :param email: Set the email address of the user
        :param password: Set the password of the user
        :return: A user object
        """
        user = self.create_user(email, password)
        # extra values being attached to make superuser
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model that supports using email instead of username

    Args:
        AbstractBaseUser ([type]): [description]
        PermissionsMixin ([type]): [description]
    """
    username = None
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    USERNAME_FIELD = 'email'
