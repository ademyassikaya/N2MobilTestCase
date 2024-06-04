from rest_framework.viewsets import ModelViewSet
from user.models import User, Company, Address
from api.user.serializers import UserSerializer, UserReadSerializer, CompanySerializer, AddressSerializer


class CompanyViewSet(ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class AddressViewSet(ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    
    def get_serializer_class(self):
        if self.action in ('create', 'update', 'delete'):
            return UserSerializer
        else:
            return UserReadSerializer

