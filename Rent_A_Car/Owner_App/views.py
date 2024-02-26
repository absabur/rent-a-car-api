from django.shortcuts import render
from rest_framework import generics
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from Owner_App.serializers import *
from Owner_App.models import *
from Client_App.models import Booking
from rest_framework import status

class IsRequestedUser(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.is_authenticated and request.user == obj.user

class HasSpecialPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        # Add your custom permission logic here
        if request.user.role == 'owner':
            return True
        return False# Example: Return True if the user has special permission


class CarViewSet(viewsets.ModelViewSet):
    serializer_class = CarSerializer
    def get_permissions(self):
        if self.action in ['list', 'retrieve', 'update', 'destroy', 'create']:
            # Require authentication and check if the user is the owner of the car
            return [permissions.IsAuthenticated(), IsRequestedUser(), HasSpecialPermission()]
        return super().get_permissions()
    def get_queryset(self):
        user = self.request.user
        queryset = Car.objects.filter(user__id=user.id)
        return queryset
    
    
class AllCarView(APIView):
    def get(self, request):
        all_car = Car.objects.all()
        serial_data = AllCarSerializer(all_car, many=True)
        return Response(serial_data.data)
    
class AllCategoryView(APIView):
    def get(self, request):
        cate = Category.objects.all()
        serial_data = AllCategorySerializer(cate, many=True)
        return Response(serial_data.data)
    

from datetime import datetime, timedelta
class BookingView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def create(self, request, *args, **kwargs):
        car = request.data.get('car')
        car_data = Car.objects.get(id=car)
        if car_data.out_of_service:
            return Response({"message": "This car is out of service."}, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, headers=headers)
   


class BookingDateListView(APIView):
    def get(self, request, **kwargs):
        car = kwargs.get('car')
        bookings = Booking.objects.filter(car=car)
        result = []
        for item in bookings:
            end = datetime.strptime(str(item.end_date), '%Y-%m-%d')
            if end > datetime.now():
                result.append(item)
        serializer = BookingDateListSerializer(result, many=True)
        return Response(serializer.data)
    
    

class BookingListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, **kwargs):
        owner = request.query_params.get('owner')
        user = request.query_params.get('user')
        if owner:
            if request.user.role != 'owner':
                return Response({"message": "You don't have permission to access this page."})
            booking = Booking.objects.filter(owner=owner)
        elif user:
            booking = Booking.objects.filter(user=user)
        else:
            booking = Booking.objects.none()
        serializer = BookingDateListSerializer(booking, many=True)
        return Response(serializer.data)
    
    

