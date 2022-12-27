from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.conf import settings


class UserProfileManager(BaseUserManager):
    """Manager for the user profiles"""

    def create_user(self, email, name, password = None):
        # create_user is an inbuilt function name for creating a new user in the user profile manager 
        """Create a new user profile """
        if not email:
            raise ValueError('User must have an email address')
            # if the user does not enter an email, which is our username field or compulsory field, normally 
            # username is the compulsory field in the default user provided but because we have our own profile manager wen specified email as ours
            
            #raise a value error 
        email = self.normalize_email(email)
        # normalize email, making the required parts that should be case sensitive, case sensitive when users type "
        user = self.model(email=email, name =name )
       
        #creating a new  model that the user manager is representing 
        #self. model is set to the model that the manager is for
        # will create auser model set the email and name since those are the major fields we created models for 

        user.set_password(password)
        # set_password comes with abstract base user, for encrypting 
        # password is converted to hash and never stored as a plain text

        user.save(using=self._db)

        # make it open to using more than one db
        #standard procedure for savimg in django 

        return user 

    def create_superuser(self, email, name, password ):
        # no password = none since it is compulsory for a super user to have a password 
        """Create and save a super user"""
        user = self.create_user(email, name , password )
        # No need for self again when using create_user, because since its in the same class, self is automatically added 
        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)

        return user



class UserProfile(AbstractBaseUser,PermissionsMixin):
    """ Creating models for database"""
    email = models.EmailField(max_length=225,unique= True)
    name = models.CharField(max_length=225, unique= True)
    is_active= models.BooleanField(default= True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)



    objects = UserProfileManager()


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']


    def get_full_name(self):
        """Return Full name"""
        return self.name


    def __str__(self):
        """Return String representation """
        return self.email
        



# Create your models here.
class ProfileFeed(models.Model):
    """Profile status update"""

    userProfile = models.ForeignKey(
        # Instead of writing the model straight go through settings.py
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    status_text = models.CharField(max_length=225)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.status_text