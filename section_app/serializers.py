from rest_framework import serializers
from .models import section_model

class sectionSerializer(serializers.ModelSerializer):
    created_on = serializers.IntegerField(read_only=True)
    class Meta:
        model= section_model
        fields= "__all__"