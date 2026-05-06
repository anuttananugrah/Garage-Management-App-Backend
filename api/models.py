from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Customer(models.Model):
    name=models.CharField(max_length=100)
    phone=models.CharField(max_length=20)
    vehicle_reg_no=models.CharField(max_length=100)
    vehicle_image=models.ImageField(upload_to="vehicle_image")
    vehicle_model_name=models.CharField(max_length=100)
    vehicle_year=models.CharField(max_length=50)
    mechanic=models.ForeignKey(User,on_delete=models.CASCADE)


class Services(models.Model):
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=500)
    service_charge=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)
    status=models.CharField(max_length=20,default="Pending")
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)

