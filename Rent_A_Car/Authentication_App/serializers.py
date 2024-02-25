from rest_framework import serializers

from Authentication_App.models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})
    class Meta:
        model = User
        fields = ('id', 'email', 'password', 'name', 'role', 'phone')
        
    def create(self, validated_data):
        email = validated_data['email']
        password = validated_data['password']
        name = validated_data['name']
        role = validated_data['role']
        phone = validated_data['phone']
        user = User.objects.create_user(email, password, name, role, phone)
        return user
    