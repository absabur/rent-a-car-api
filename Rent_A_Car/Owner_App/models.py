from django.db import models
from Authentication_App.models import User
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Car(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cars')
    car_name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    image = models.ImageField(upload_to='cars', blank=True)
    engine_cc = models.FloatField()
    number_of_seats = models.IntegerField()
    out_of_service = models.BooleanField(default=False)
    per_day_rent = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.car_name
    
    class Meta:
        ordering = ['out_of_service', '-updated_at', '-created_at']