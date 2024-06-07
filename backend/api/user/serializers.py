from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField
from user.models import User, Company, Address, Geo

class CompanySerializer(ModelSerializer):
    class Meta:
        model = Company
        fields = ["id", "name"]

class CompanyNameSerializer(ModelSerializer):
    class Meta:
        model = Company
        fields = ["name"]

class GeoSeriilizer(ModelSerializer):
    class Meta:
        model = Geo
        fields = ["lat", "lng"]

class AddressSerializer(ModelSerializer):
    geo = GeoSeriilizer()
    class Meta:
        model = Address
        fields = ["street", "suite", "city", "zipcode", "geo"]


class UserSerializer(ModelSerializer):
    company = CompanyNameSerializer()
    address = AddressSerializer()
    class Meta:
        model = User
        fields = ["id", "name", "username", "email","address", "phone", "website", "company"]


class UserReadSerializer(ModelSerializer):
    company = CompanyNameSerializer(read_only=True)
    address = AddressSerializer(read_only=True)
    class Meta:
        model = User
        fields = ["id", "name", "username", "email","address", "phone", "website", "company"]

        