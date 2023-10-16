from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


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
            username = username
        )
        user.set_password(password)
        user.is_staff()
        user.is_superuser = True
        user.save()
        return user


# my  user model
class User(AbstractBaseUser):
    username = models.CharField(unique=False, max_length=25, blank=False)
    email = models.EmailField(unique=True, max_length=25, blank=False)
    password = models.CharField(max_length=15, blank=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["password"]

    def __str__(self) -> str:
        return self.username
    

# additional information for the userprofile
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(blank=True, null=True)
    bio = models.TextField(max_length=75, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.user.username