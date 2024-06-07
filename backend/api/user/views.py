from rest_framework.viewsets import ModelViewSet
from user.models import User, Company, Address
from api.user.serializers import UserSerializer, UserReadSerializer, CompanySerializer, AddressSerializer
from user.models import Geo  # Geo modelini ekledik

class CompanyViewSet(ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class AddressViewSet(ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.action in ['create', 'update']:
            return UserSerializer
        else:
            return UserReadSerializer

    def perform_create(self, serializer):
        company_data = serializer.validated_data.pop('company')
        address_data = serializer.validated_data.pop('address')
        company = Company.objects.create(**company_data)
        
        # Geo verilerini al
        geo_data = address_data.pop('geo')
        geo_instance = Geo.objects.create(**geo_data)
        
        # Address oluştur
        address = Address.objects.create(geo=geo_instance, **address_data)
        
        serializer.save(company=company, address=address)

    def perform_update(self, serializer):
        company_data = serializer.validated_data.pop('company')
        address_data = serializer.validated_data.pop('address')
        company_instance = serializer.instance.company
        address_instance = serializer.instance.address
        
        # Company güncelle
        for attr, value in company_data.items():
            setattr(company_instance, attr, value)
        company_instance.save()
        
        # Geo güncelle
        geo_data = address_data.pop('geo')
        geo_instance = address_instance.geo
        for attr, value in geo_data.items():
            setattr(geo_instance, attr, value)
        geo_instance.save()
        
        # Address güncelle
        for attr, value in address_data.items():
            setattr(address_instance, attr, value)
        address_instance.save()
        
        serializer.save()
