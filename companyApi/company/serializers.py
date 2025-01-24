from rest_framework import serializers
from .models import companyModel , EmployeeModel

class companySerializer(serializers.ModelSerializer):
    class Meta:
        model=companyModel
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=EmployeeModel
        fields='__all__'