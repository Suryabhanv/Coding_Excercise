# api/views.py

from rest_framework import viewsets
from .models import Company, Client, ClientUser
from .serializers import CompanySerializer, ClientSerializer, ClientUserSerializer

# api/views.py

from rest_framework.permissions import IsAdminUser

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [IsAdminUser]

# Define other views with appropriate permissions as required

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class ClientUserViewSet(viewsets.ModelViewSet):
    queryset = ClientUser.objects.all()
    serializer_class = ClientUserSerializer

# Define other views as required
