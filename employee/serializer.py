from rest_framework.serializers import ModelSerializer
from employee.models import Employee

# Serializer for Employee Table
class EmployeeSerializer(ModelSerializer):

    class Meta:
        model = Employee
        fields = '__all__'
