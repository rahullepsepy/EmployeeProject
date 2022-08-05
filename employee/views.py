from django.shortcuts import render

# Create your views here.
'''
Employee:
    id
    name
    address

We have to create two API for GET and POST
'''
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from employee.models import Employee
from employee.serializer import EmployeeSerializer


# APIs for Employee Model
class EmployeeView(APIView):

    def get(self, request):
        id = request.GET.get('id', None)
        if id:
            emp = Employee.objects.filter(id=id)
            if emp.exists():
                serializer = EmployeeSerializer(emp.first())
                return Response({'status': 200, 'data':serializer.data}, status = status.HTTP_200_OK)
                
            return Response({'status': 404, 'data': f"Not Found! for {id}, Please check the ID"}, status = status.HTTP_404_NOT_FOUND)

        emps = Employee.objects.all()
        serializer = EmployeeSerializer(emps, many=True)
        return Response({'status': 200, 'data':serializer.data}, status = status.HTTP_200_OK)

    def post(self, request):
        name = request.data.get('name')
        address = request.data.get('address')
        data = {"name": name, "address": address}

        serializer = EmployeeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 201, 'data': serializer.data}, status = status.HTTP_201_CREATED)
            
        return Response({'status': 400, 'data': serializer.errors}, status = status.HTTP_400_BAD_REQUEST)
