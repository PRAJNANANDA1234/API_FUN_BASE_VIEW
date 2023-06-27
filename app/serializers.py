from app.models import *
from rest_framework import serializers

class EmpMS(serializers.ModelSerializer):
    class Meta:
        model=Employees
        fields='__all__'