from rest_framework import status
from rest_framework.response import Response
from rest_framework.settings import api_settings
from django.contrib.auth import authenticate
from django.forms.models import model_to_dict
from rest_framework.decorators import action

from ggachiauth.models import User
from .serializers import LetterSerializer

class ListModelMixin:
    def list(self, request, *args, **kwargs):
        authenticate_kwargs = {
            'email': request.data['email'],
            'password': request.data['password'],
        }
        user = authenticate(**authenticate_kwargs)
        if user is None:
            return Response({'user': 'is none'}, status=status.HTTP_401_UNAUTHORIZED)

        queryset = self.filter_queryset(self.get_queryset())
        queryset = queryset.filter(user=user)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['post'])
    def mine(self, request):
        authenticate_kwargs = {
            'email': request.data['email'],
            'password': request.data['password'],
        }
        user = authenticate(**authenticate_kwargs)
        if user is None:
            return Response({'user': 'is none'}, status=status.HTTP_401_UNAUTHORIZED)

        queryset = self.filter_queryset(self.get_queryset())
        queryset = queryset.filter(user=user)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class CreateModelMixin:
    def perform_create(self, serializer, user):
        return serializer.save(user=user)

    def create(self, request, *args, **kwargs):
        authenticate_kwargs = {
            'email': request.data['email'],
            'password': request.data['password1'],
        }
        if request.data['password1'] != request.data['password2']:
            return Response({'password': 'not same'}, status=status.HTTP_400_BAD_REQUEST)
        user = authenticate(**authenticate_kwargs)
        if user is None:
            user = User.objects.create_user(**authenticate_kwargs)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        new_letter = model_to_dict(self.perform_create(serializer, user))
        return Response(new_letter)
            
    