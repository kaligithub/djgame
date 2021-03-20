from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from play.employee.models import Employee
from play.employee.serializers import EmplyoeeSerializer

from play.base import pagination, response


class EmployeeViewSet(viewsets.ModelViewSet):

    queryset = Employee.objects.all()
    serializer_class = EmplyoeeSerializer
    #permission_classes = [IsAuthenticated]
    
    def list(self, request):
        
        return response.Ok({'ok':'list'})

    def create(self, request):
        #import pdb; pdb.set_trace()
        
        req_data = self.request.data
        serializer = EmplyoeeSerializer(
            data = req_data,

        )

        serializer.is_valid(raise_exception=True)
            
        serializer.save()

        return response.Ok(serializer.data)


    def retrieve(self, request, pk=None):
        
        return response.Ok({'ok':'retrieve'})


    def update(self, request, pk=None):
        
        return response.Ok({'ok':'update'})

    def partial_update(self, request, pk=None):
        
        return response.Ok({'ok':'patial_update'})

    def destroy(self, request, pk=None):
        
        return response.Ok({'ok':'delete'})
