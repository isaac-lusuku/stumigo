from .models import *
from main.models import User


class Activate:
    def __init__(self, email) -> None:
        self.email = email

    # the function to return the room to participate in
    def room_in(self):
        user = User.objects.get(email=self.email)
        rooms_in = user.room_set.all()

    def room_recommendations(self):
        