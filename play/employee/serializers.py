from rest_framework import serializers

from play.employee.models import Employee


class EmplyoeeSerializer(serializers.ModelSerializer):

    age = serializers.IntegerField()

    loan_schema = {
        '$schema': 'http://json-schema.org/draft-04/schema#',
        'title': 'Employee',
        'description': 'Employee details JSON',
        'type': 'object',
        'properties': {
            'regNo': {
                'type': 'integer',
            },
            'name': {
                'type': 'string',
            },
            'email': {
                'type': 'string',
            },
            'mobile': {
                'type': 'integer',
            },

        },
    }

    class Meta:
        model = Employee
        fields = '__all__'

    
    def age_validation(self, age: int) -> int:

        if not isinstance(age, int):
            raise serializers.ValidationError(_("Age is not Integer"))

        return age    


        



