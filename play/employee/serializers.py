from rest_framework import serializers

from play.employee.models import Employee


class EmplyoeeSerializer(serializers.ModelSerializer):

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

        



