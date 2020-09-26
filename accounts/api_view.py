from rest_framework.generics import CreateAPIView,UpdateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .serializers import UserCreateSerializer,UserPasswordChangeSerializer
from .models import User, ActivationToken

class CreateUserAPIView(CreateAPIView):
    """
    API to create user with email verification
    """
    serializer_class = UserCreateSerializer
    queryset = User.objects.all()

class Activate(APIView):
    """
    API to activate user after registration with token sent to user email
    """
    def post(self,request):
        user_token = request.data['token']
        email = request.data['email']
        try:
            token = ActivationToken.objects.get(token=user_token)
            user = User.objects.get(email=email)
        except:
            return Response({'message':'TOKEN OR USER NOT FOUND'})
        user.is_active = True
        user.save()
        token.delete()
        return Response({'message': 'ACCOUNT ACTIVATE' })

class ChangePassword(APIView):
    """
    API to Change user's password with JWT Token
    """
    permission_classes = [IsAuthenticated]
    serializer_class = UserPasswordChangeSerializer
    def put(self,request):
        try:
            user = User.objects.get(email=request.data['email'])
        except:
            return Response({"message":"User NOT FOUND"})
        ser = UserPasswordChangeSerializer(user,data=request.data, partial=True)
        if ser.is_valid():
            ser.save()
            return Response({"message":"Password Update"})
        return Response({"message":"BAD REQUEST"})

