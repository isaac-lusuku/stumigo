from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
import datetime


# my usermanager
class MyUserManager(BaseUserManager):

    def creat_user(self, email, username, password):
        if not email or not username or not password:
            raise ValueError("one of the fields was missing")
        user = self.model(
            email = self.normalize_email(email), 
            username = username
        )
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, username, password):
        if not email or not username or not password:
            raise ValueError("one of the fields was missing")
        user = self.model(
            email = self.normalize_email(email), 
        )
        user.username = username
        user.set_password(password)
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user


# my  user model
class User(AbstractBaseUser):
    email = models.EmailField(unique=True, max_length=25, blank=False)
    password = models.CharField(max_length=150, blank=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["password",]

    objects = MyUserManager()

    def __str__(self) -> str:
        return self.username
    
    def is_staff():
        is_staff = True
        return is_staff
    
    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser
    

# additional information for the userprofile
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(blank=True, null=True)
    bio = models.TextField(max_length=75, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True, null=True)
    study_mate = models.ManyToManyField("self", blank=True)
    followers = models.ManyToManyField("self", blank=True)
    username = models.CharField(unique=False, max_length=25, blank=False)

    def __str__(self) -> str:
        return self.user.username

    
