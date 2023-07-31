from rest_framework import viewsets, status
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from .models import Elevator, Floor, UserRequest
from .serializers import ElevatorSerializer, FloorSerializer, UserRequestSerializer

class ElevatorViewSet(viewsets.ModelViewSet):
    queryset = Elevator.objects.all()
    serializer_class = ElevatorSerializer

    @action(detail=False, methods=['post'])
    def initialize_elevator_system(self, request):
        num_elevators = request.data.get('num_elevators', 0)
        for _ in range(num_elevators):
            Elevator.objects.create()
        return Response({'message': f'{num_elevators} elevators initialized successfully.'}, status=status.HTTP_201_CREATED)

class FloorViewSet(viewsets.ModelViewSet):
    queryset = Floor.objects.all()
    serializer_class = FloorSerializer

class UserRequestViewSet(viewsets.ModelViewSet):
    queryset = UserRequest.objects.all()
    serializer_class = UserRequestSerializer

@api_view(['POST'])
def initialize_elevator_system_view(request):
    # Implement the logic to initialize the elevator system
    # For example, you can create 'n' elevators in the system here
    num_elevators = request.data.get('num_elevators', 0)
    # Your logic to initialize 'n' elevators goes here...

    # Return a response with a success message
    response_data = {"message": f"{num_elevators} elevators initialized successfully."}
    return Response(response_data, status=status.HTTP_201_CREATED)
