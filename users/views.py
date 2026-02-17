from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User

from .models import ConfirmCode
from .serializers import UserCreateSerializer,ConfirmcodeSerializer

@api_view(['POST'])
def registration_api_view(req):
    serializer = UserCreateSerializer(data=req.data)
    serializer.is_valid(raise_exception=True)

    username = serializer.validated_data['username']
    password = serializer.validated_data['password']

    user = User.objects.create_user(username=username,password=password,is_active = False)
    ConfirmCode.objects.create(username=username)

    return Response(status=status.HTTP_201_CREATED,
                    data={'user_id':user.id})

@api_view(['POST', 'GET'])
def autherithezion_api_view(req):
    if req.method == 'POST':
        serializer = ConfirmcodeSerializer(data=req.data)
        user = serializer.is_valid(raise_exception=True)
        
        return Response(status=status.HTTP_201_CREATED,
                        data=user)
    elif req.method == 'GET':
        user_id = req.query_params.get('user_id')

        code = ConfirmCode.objects.get(user_id=int(user_id))
        
        return Response(status=status.HTTP_201_CREATED, data=code.code)
    