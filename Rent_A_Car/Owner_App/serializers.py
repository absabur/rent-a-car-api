from rest_framework import serializers
from Owner_App.models import *
from Client_App.models import Booking
from Authentication_App.serializers import UserSerializer

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'
        

class AllCarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'
        
class AllCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        
        
class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'
        
        
class BookingDateListSerializer(serializers.ModelSerializer):
    car = CarSerializer()
    user = UserSerializer()
    class Meta:
        model = Booking
        fields = '__all__'
        
