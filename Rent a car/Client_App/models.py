from django.db import models
from Authentication_App.models import User
from Owner_App.models import Car

# Create your models here.
class Booking(models.Model):
    user = models.ForeignKey(User, related_name='bookings', on_delete=models.CASCADE)
    car = models.ForeignKey(Car, related_name='car', on_delete=models.CASCADE)
    owner = models.ForeignKey(User, related_name='owners', on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    class Meta:
        ordering = ['-created_at', '-start_date', '-end_date']