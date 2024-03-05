from django.db import models
from email.policy import default
from django.contrib.auth.models import User

# Create your models here.

CATEGORY=(
    ("Ok_Food", "Ok_Food"),
    ("Oxford", "Oxford"),
    ("Mamuda", "Mamuda"),
    ("Pordee_Food_NIGERIA", "Pordee_Food_Nigeria"),
    ("Beloxy", "Beloxy"),
    ("New_Bisco", "New_Bisco"),
    ("Sumal_Yale", "Sumal_Yale"),
)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    physical_address= models.CharField(max_length=100, null=True)
    mobile=models.CharField(max_length=15, null=True)
    

    def __str__(self) -> str:
        return self.user.username
    
class Product(models.Model):
    name=models.CharField(max_length=150, null=True)
    category= models.CharField(max_length= 30, choices=CATEGORY, null=True)
    quantity= models.PositiveIntegerField(null=True)
    description= models.CharField(max_length=300, null=True)
    price=models.DecimalField(max_digits=20, decimal_places=2)

    def __str__(self) -> str:
        return self.name
    
class Order(models.Model):
    product= models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    created_by=models.ForeignKey(User, models.CASCADE, null=True)
    order_quantity= models.PositiveIntegerField(null=True)
    price=models.DecimalField(max_digits=20, decimal_places=2)
    date= models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.product} ordered quantity {self.order_quantity}"


