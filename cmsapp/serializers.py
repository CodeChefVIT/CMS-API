from rest_framework import serializers
from .models import Details


class DetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Details
        fields = ['rfid', 'name', 'event_name', 'registration_number', 'phone_number', 'email']