from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.conf import settings


#managers
class UserProfileManager(BaseUserManager):
    """Manager for UserProfile """

    # Another thing to note is that Manager methods
    # can access self.model to get the model class to which
    # they’re attached.

    def create_user(self,email,name,password=None):
        """Create a new user profile"""

        if not email:
            raise ValueError("User must have an email address")

        #normalizing email's second half i.e will convert to lower case the @ part of the email id
        email = self.normalize_email(email)
        user = self.model(email = email , name = name) #returning object of model to which it is linked

        user.set_password(password) #to encrypt the password
        user.save(using = self._db)

        return user


    def create_superuser(self,email, name,password):
        """Create and save new super user with provided details"""

        user = self.create_user(email, name, password)

        user.is_superuser = True #inheriting from PermissionsMixin
        user.is_staff = True
        user.save(using=self._db)


        return user





# Create your models here.
class UserProfile(AbstractBaseUser,PermissionsMixin):
    """
        Database model for users in the system
    """
    email = models.EmailField(max_length = 255, unique = True)
    name = models.CharField(max_length = 255)
    is_active = models.BooleanField(default  = True)
    is_staff = models.BooleanField(default = False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """
        Retrieve full name of the user
        """
        return self.name


    def get_short_name(self):
        """Retrieve shorter name of user """
        return self.name


    def __str__(self):
        """Return string representation of the user """
        return self.email


class ProfileFeedItem(models.Model):
    """Profile status update"""

    #in the ForeignKey as we knwo thatwe have to specify the model anme to which we want to link.
    # here I can directly use 'UserProfile' model class to which  I want to linked
    #but the best practices is always to get this name from settings file/
    # so that if in fututre if we change user authentication model then we do not need to change
    # every occurence of that in code. we can directly change in settings.py file and it will reflect everywhere.
    
    user_profile = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete = models.CASCADE
    )
    status_text = models.CharField(max_length = 255)
    created_on = models.DateField(auto_now_add = True)


    def __str__(self):
        """Return the model as a a string """
        return self.status_text
