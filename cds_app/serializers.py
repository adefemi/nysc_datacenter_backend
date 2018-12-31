from rest_framework import serializers
from .models import cds_model

class cdsSerializer(serializers.ModelSerializer):
    created_on = serializers.IntegerField(read_only=True)
    updated_on = serializers.IntegerField(read_only=True)
    class Meta:
        model= cds_model
        fields= "__all__"