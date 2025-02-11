from rest_framework import serializers
from .models import Poet

class PoetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poet
        fields = '__all__'