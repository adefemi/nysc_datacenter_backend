from rest_framework import serializers
from .models import Members_app
from cds_app.serializers import cdsSerializer
from section_app.serializers import sectionSerializer

class corpsSerializer(serializers.ModelSerializer):
    created_on = serializers.IntegerField(read_only=True)
    updated_on = serializers.IntegerField(read_only=True)
    section = sectionSerializer
    cds_group = cdsSerializer
    class Meta:
        model= Members_app
        fields= "__all__"