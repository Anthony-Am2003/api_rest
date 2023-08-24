from rest_framework import viewsets
from .serializaer import CompanySerializer
from .models import Company

# Create your views here.

class CompanyViews(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer