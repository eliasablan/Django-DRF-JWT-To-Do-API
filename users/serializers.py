from django.contrib.auth.models import User
from rest_framework import serializers
from decouple import config as dc_config

SUPERUSER_EMAIL = dc_config('SUPERUSER_EMAIL')

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=False)

    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'is_superuser', 'is_staff')

    def validate(self, data):
        # Comprueba si el correo electrónico ya está en uso.
        existing_user = User.objects.filter(email=data['email']).first()
        if existing_user:
            # Si el correo electrónico ya está en uso, lanza un error.
            raise serializers.ValidationError({'email': ['El correo electrónico ya está en uso.']})

        # Comprueba si el correo electrónico coincide con el SUPERUSER_EMAIL.
        if data['email'] == SUPERUSER_EMAIL:
            data['is_superuser'] = True
            data['is_staff'] = True

        return data