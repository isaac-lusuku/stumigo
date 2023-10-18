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
    study_mate = models.ManyToManyField("self", blank=True)

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


# topics for discussion
class Topic(models.Model):
    name = models.CharField(blank=False, max_length=25)

    def __str__(self):
        return self.name


#problems that are put up for discussion
class Problem(models.Model):
    asked_by = models.ForeignKey(User, blank=True, on_delete=models.SET_NULL, null=True)
    question = models.TextField(max_length=100, blank=None)
    time_asked = models.DateTimeField(auto_now_add=True)
    topic = models.ForeignKey(Topic, blank=True, null=True, on_delete=models.SET_NULL)

    class Meta:
        ordering = ['-time_asked'] 

    def __str__(self):
        return self.question[20]


# the solutions to the problems pu up
class Solution(models.Model):
    answered_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    problem = models.ForeignKey(Problem, blank=False, on_delete=models.CASCADE)
    answered_at = models.DateTimeField(auto_now_add=True)
    up_vote = models.IntegerField(default=0)
    down_vote = models.IntegerField(default=0)
    answer = models.TextField(blank=False, max_length=150)

    class Meta:
        ordering = ['-answered_at'] 

    def __str__(self):
        return self.answer[20]


# the discussion rooms for various topics
class Room(models.Model):
    name = models.CharField(max_length=25, blank=False)
    created_by = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, blank=True, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    members = models.ManyToManyField(User, blank=True, related_name="participants")
    description = models.TextField(max_length=100, blank=True)

    def __str__(self):
        return self.name
    

# messages belonging to different rooms
class Message(models.Model):
    creator = models.ForeignKey(User, blank=False, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, blank=False, on_delete=models.CASCADE)
    body = models.TextField(max_length=250, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    replied_to = models.ForeignKey("self", blank=True, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-created_at'] 

    def __str__(self):
        return self.body[20]
    

    class Message(models.Model):
    creator = models.ForeignKey(User, blank=False, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, blank=False, on_delete=models.CASCADE)
    body = models.TextField(max_length=250, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    replied_to = models.ForeignKey("self", blank=True, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-created_at'] 

    def __str__(self):
        return self.body[20]