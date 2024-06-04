from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField
from user.models import User, Company, Address

class CompanySerializer(ModelSerializer):
    class Meta:
        model = Company
        fields = ["id", "name"]

class CompanyNameSerializer(ModelSerializer):
    class Meta:
        model = Company
        fields = ["name"]

class AddressSerializer(ModelSerializer):
    class Meta:
        model = Address
        fields = ["street", "suite", "city", "zipcode"]


class UserSerializer(ModelSerializer):
    company = PrimaryKeyRelatedField(queryset=Company.objects.all())
    address = PrimaryKeyRelatedField(queryset=Address.objects.all())
    class Meta:
        model = User
        fields = ["id", "name", "username", "email","address", "phone", "website", "company"]


class UserReadSerializer(ModelSerializer):
    company = CompanyNameSerializer(read_only=True)
    address = AddressSerializer(read_only=True)
    class Meta:
        model = User
        fields = ["id", "name", "username", "email","address", "phone", "website", "company"]