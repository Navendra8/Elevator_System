from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Elevator, Floor, UserRequest

class ElevatorSystemTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_initialize_elevator_system(self):
        # Send a POST request to initialize the elevator system with 3 elevators
        response = self.client.post('/api/elevators/initialize_elevator_system/', {'num_elevators': 3}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], "3 elevators initialized successfully")

        # Verify that 3 elevators are created in the database
        elevators = Elevator.objects.all()
        self.assertEqual(elevators.count(), 3)

    def test_get_all_elevators(self):
        # Assuming there are 3 elevators in the system
        Elevator.objects.bulk_create([
            Elevator(operational=True),
            Elevator(operational=True),
            Elevator(operational=True)
        ])

        # Send a GET request to get all elevators
        response = self.client.get('/api/elevators/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Verify that the response contains 3 elevators
        self.assertEqual(len(response.data), 3)

    def test_get_all_floors(self):
        # Assuming there is one floor with number 1 in the system
        Floor.objects.create(number=1)

        # Send a GET request to get all floors
        response = self.client.get('/api/floors/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Verify that the response contains one floor with number 1
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['number'], 1)

    def test_get_all_user_requests(self):
        # Assuming there is one user request with floor 1 and direction 'UP' in the system
        UserRequest.objects.create(floor=1, direction='UP')

        # Send a GET request to get all user requests
        response = self.client.get('/api/user-requests/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Verify that the response contains one user request with floor 1 and direction 'UP'
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['floor'], 1)
        self.assertEqual(response.data[0]['direction'], 'UP')

    def test_add_user_request(self):
        # Send a POST request to add a user request with floor 3 and direction 'UP'
        data = {'floor': 3, 'direction': 'UP'}
        response = self.client.post('/api/user-requests/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Verify that the user request is created in the database
        user_request = UserRequest.objects.get(pk=response.data['id'])
        self.assertEqual(user_request.floor, 3)
        self.assertEqual(user_request.direction, 'UP')

    def test_invalid_user_request(self):
        # Send a POST request with an invalid user request (invalid floor number 0)
        data = {'floor': 0, 'direction': 'UP'}
        response = self.client.post('/api/user-requests/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # Send a POST request with an invalid user request (missing direction)
        data = {'floor': 3}
        response = self.client.post('/api/user-requests/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_fetch_next_destination_floor_for_elevator(self):
        # Assuming elevator 1 is operational and there's a user request for floor 4
        elevator = Elevator.objects.create(operational=True)
        UserRequest.objects.create(floor=4, direction='UP')

        # Send a GET request to get the next destination floor for elevator 1
        response = self.client.get(f'/api/elevators/{elevator.id}/next-destination/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Verify that the response contains the next destination floor (floor 4) and direction 'UP'
        self.assertEqual(response.data['next_floor'], 4)
        self.assertEqual(response.data['direction'], 'UP')

    def test_mark_elevator_as_not_working(self):
        # Assuming elevator 1 is operational
        elevator = Elevator.objects.create(operational=True)

        # Send a PATCH request to mark elevator 1 as not working
        response = self.client.patch(f'/api/elevators/{elevator.id}/mark-not-working/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Verify that elevator 1 is marked as not operational in the database
        elevator.refresh_from_db()
        self.assertFalse(elevator.operational)

    def test_open_close_elevator_door(self):
        # Assuming elevator 1 is operational
        elevator = Elevator.objects.create(operational=True)

        # Send a PATCH request to open and close the door for elevator 1
        response = self.client.patch(f'/api/elevators/{elevator.id}/open-door/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = self.client
