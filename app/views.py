from django.shortcuts import render

from app.models import *
from app.serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
# Create your views here.
@api_view()
@permission_classes([IsAuthenticated])
def employee(request):
    ESQ=Employees.objects.all()
    ESD=EmpMS(ESQ,many=True)
    return Response(ESD.data)
 