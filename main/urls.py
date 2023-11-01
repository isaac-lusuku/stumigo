from django.urls import path, include
from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('users/', UserView.as_view(), name="users")
]

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