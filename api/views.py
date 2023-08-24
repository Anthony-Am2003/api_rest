from rest_framework import viewsets
from .serializaer import CompanySerializer
from .models import Company
from django.contrib.auth.models import User
from .serializaer import UserSerializer

# Create your views here.

class CompanyViews(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class UserViews(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer