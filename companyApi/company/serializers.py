from rest_framework import serializers
from .models import companyModel

class companySerializer(serializers.ModelSerializer):
    class Meta:
        model=companyModel
        fields = '__all__'
