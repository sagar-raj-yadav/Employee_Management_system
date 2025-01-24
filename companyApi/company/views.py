from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .serializers import companySerializer , EmployeeSerializer
from .models import companyModel , EmployeeModel

@api_view(['GET'])
def home_page(request):
    return Response( "Hello, world!")

#company views
@api_view(['POST'])
def create_company(request):
    serializer=companySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message":"company added sucessfully","data":serializer.data},status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_company(request):
    company=companyModel.objects.all()
    serializer=companySerializer(company,many=True)
    return Response({'msg': 'Successfully retrieved data', 'data': serializer.data}, status=status.HTTP_200_OK)

@api_view(['PUT'])
def update_company(request):
    company=companyModel.objects.get(pl=request.data.get('id'))
    serializer=companySerializer(company,many=True)
    if serializer.is_valid():
        serializer.save()
        return Response({'msg': 'company updated successfully', 'data': serializer.data}, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_company(request):
    company=companyModel.objects.get(pl=request.data.get('id'))
    company.delete()
    return Response({'msg': 'company deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
    return Response({'msg': 'Invalid request method'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)



#employees views
@api_view(['POST'])
def create_employee(request):
    serializer=EmployeeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'msg': 'employee updated successfully', 'data': serializer.data}, status=status.HTTP_200_OK) 
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_employee(request):
    employee=companyModel.objects.all()
    serializer=EmployeeSerializer(employee,many=True)
    return Response({'msg': 'Successfully retrieved data', 'data': serializer.data}, status=status.HTTP_200_OK)

@api_view(['PUT'])
def update_employee(request):
    serializer=EmployeeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'msg': 'employee updated successfully', 'data': serializer.data}, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_employee(request):
    employee=EmployeeModel.objects.get(pl=request.data.get('id'))
    employee.delete()
    return Response({'msg': 'employee deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
    return Response({'msg': 'Invalid request method'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
