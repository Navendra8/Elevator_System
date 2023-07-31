from rest_framework import serializers
from .models import Elevator, Floor, UserRequest

class ElevatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Elevator
        fields = '__all__'

class FloorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Floor
        fields = '__all__'

class UserRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRequest
        fields = '__all__'

class InitializeElevatorSystemSerializer(serializers.Serializer):
    num_elevators = serializers.IntegerField()
