from __future__ import print_function
"""
    in this file i write all me  views to serve my API
"""

from .models import *
from django.db.models import Q
from .serializers import *
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.views import APIView
import re

"""
remember to read about OAUTH and implement it in the code
"""
# import base64
# from email.message import EmailMessage

# import google.auth
# from googleapiclient.discovery import build
# from googleapiclient.errors import HttpError


# def gmail_send_message():
#     """Create and send an email message
#     Print the returned  message id
#     Returns: Message object, including message id

#     Load pre-authorized user credentials from the environment.
#     TODO(developer) - See https://developers.google.com/identity
#     for guides on implementing OAuth2 for the application.
#     """
#     creds, _ = google.auth.default()

#     try:
#         service = build('gmail', 'v1', credentials=creds)
#         message = EmailMessage()

#         message.set_content('This is automated draft mail')

#         message['To'] = 'gduser1@workspacesamples.dev'
#         message['From'] = 'gduser2@workspacesamples.dev'
#         message['Subject'] = 'Automated draft'

#         # encoded message
#         encoded_message = base64.urlsafe_b64encode(message.as_bytes()) \
#             .decode()

#         create_message = {
#             'raw': encoded_message
#         }
#         # pylint: disable=E1101
#         send_message = (service.users().messages().send
#                         (userId="me", body=create_message).execute())
#         print(F'Message Id: {send_message["id"]}')
#     except HttpError as error:
#         print(F'An error occurred: {error}')
#         send_message = None
#     return send_message


# if __name__ == '__main__':
#     gmail_send_message()



# function to validat the email address that was entered 
def is_valid_email(email):
    # Define a regular expression for basic email validation
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None


# this creates and returns the user 
class UserView(APIView):
    permission_classes = [AllowAny]

    # creating a user
    def post(self, request):
        user_data = UserSerializer(data=request.data)

        # validating the email address entered 
        if is_valid_email(request.email):
            """
            after this point i should consider a verification email for 
            confirmation
            """
            if user_data.is_valid():
                user_data.save()
                return Response(status.HTTP_201_CREATED)
            else:
                return Response(status.HTTP_406_NOT_ACCEPTABLE)
        
    def get(self, request, pk):
        user = User.objects.get(id=pk)
        serializer_data = UserProfileSerializer(user, many=False).data
        return Response(serializer_data, status.HTTP_200_OK)
        

