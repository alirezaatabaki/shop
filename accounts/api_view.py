from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import UserCreateSerializer
from .models import User, ActivationToken

class CreateUserAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer
    queryset = User.objects.all()

class Activate(APIView):
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