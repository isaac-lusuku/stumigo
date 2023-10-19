from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(User)
admin.site.register(UserProfile)
admin.site.register(Topic)
admin.site.register(Problem)
admin.site.register(Solution)
admin.site.register(Room)
admin.site.register(Message)