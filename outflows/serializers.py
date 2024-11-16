from rest_framework import serializers
from .models import Outflow


class OutflowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Outflow
        fields = '__all__'
