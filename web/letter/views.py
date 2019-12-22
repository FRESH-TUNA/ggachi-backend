from rest_framework import viewsets, mixins, status
from django.shortcuts import render
from rest_framework.viewsets import GenericViewSet
from .serializers import LetterSerializer
from .mixin import CreateModelMixin, ListModelMixin
from .models import Letter

class LetterViewSet(CreateModelMixin,
                    ListModelMixin,
                    mixins.RetrieveModelMixin,
                    GenericViewSet):
    def get_queryset(self):
        return Letter.objects.all()

    def get_serializer_class(self):
        return LetterSerializer
