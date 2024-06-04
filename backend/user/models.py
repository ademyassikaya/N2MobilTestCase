from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name

class Address(models.Model):
    street = models.CharField(max_length=100)
    suite = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.street}, {self.suite}, {self.city}, {self.zipcode}"

class User(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    phone = models.CharField(max_length=100)
    website = models.CharField(max_length=100)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name