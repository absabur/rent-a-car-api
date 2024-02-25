from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from Authentication_App.models import User

from Authentication_App.serializers import UserSerializer
# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    def get_permissions(self):
        if self.action in ['retrieve', 'update', 'destroy']:
            # Require authentication for GET (retrieve), PUT (update), and DELETE requests
            return [IsAuthenticated()]
        elif self.action == 'create':
            # Allow unauthenticated users to POST (create) requests
            return [AllowAny()]
        return super().get_permissions()
    

# class OrderViewSet(viewsets.ModelViewSet):
#     permission_classes = [IsAuthenticated]
#     serializer_class = OrderSerializer
#     def get_queryset(self):
#         user = self.request.user
#         queryset = Order.objects.filter(user__id=user.id)
#         return queryset