from rest_framework import serializers
from django.db.models import Avg, F
from letter.models import Letter
from django.core.validators import MaxValueValidator, MinValueValidator

class LetterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Letter
        exclude = ['user']