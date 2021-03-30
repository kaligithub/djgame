from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from play.employee.models import Employee
from play.employee.serializers import EmplyoeeSerializer

from play.base import pagination, response
from rest_framework import status
from django.http import Http404
from rest_framework.response import Response
from rest_framework.decorators import action


class EmployeeViewSet(viewsets.ModelViewSet):

    queryset = Employee.objects.all()
    serializer_class = EmplyoeeSerializer
    permission_classes = [IsAuthenticated]
    
    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = EmplyoeeSerializer(queryset, many=True)   
        return response.Ok(serializer.data)

    def retrieve(self, request, pk=None):
        employee = self.get_object()
        serializer = EmplyoeeSerializer(instance=employee)
        return response.Ok(serializer.data)

    def create(self, request):
        #import pdb; pdb.set_trace()
        
        req_data = self.request.data
        serializer = EmplyoeeSerializer(
            data = req_data,

        )

        serializer.is_valid(raise_exception=True)
            
        serializer.save()

        return response.Ok(serializer.data)


    def update(self, request, pk=None):

        instance = self.get_object()
        serializer = EmplyoeeSerializer(
            instance=instance,
            data = request.data
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return response.Ok(serializer.data)

    def partial_update(self, request, *args, **kwargs):
    
        instance = self.get_object()
        serializer = EmplyoeeSerializer(
            instance=instance,
            data=request.data, 
            partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return response.Ok(serializer.data)


    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
        except Http404:
            pass
        return Response(status=status.HTTP_204_NO_CONTENT)

 