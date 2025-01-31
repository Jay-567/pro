from rest_framework import serializers
from detail.models import CollegeModel

class CollegeSerializer(serializers.ModelSerializer):
    class Meta:
        model=CollegeModel
        fields='__all__'