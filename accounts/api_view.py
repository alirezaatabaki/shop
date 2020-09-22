from rest_framework.generics import CreateAPIView

from .serializers import UserCreateSerializer
from .models import User

class CreateUserAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer
    queryset = User.objects.all()
    
