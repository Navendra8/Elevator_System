Sure, let's walk through the steps to create the complete elevator system project step by step:

Step 1: Set Up Django Project
1. Install Django and Django REST framework using pip:
   ```
   pip install django djangorestframework
   ```

2. Create a new Django project:
   ```
   django-admin startproject elevator_system
   ```

3. Create a new Django app within the project:
   ```
   cd elevator_system
   python manage.py startapp elevators
   ```

Step 2: Define Models
1. In `models.py` of the `elevators` app, define the models for Elevator, Floor, and UserRequest:
   ```python
   # elevators/models.py
   from django.db import models

   class Elevator(models.Model):
       operational = models.BooleanField(default=True)

   class Floor(models.Model):
       number = models.PositiveIntegerField(unique=True)

   class UserRequest(models.Model):
       floor = models.ForeignKey(Floor, on_delete=models.CASCADE)
       direction = models.CharField(choices=[('UP', 'Up'), ('DOWN', 'Down')], max_length=4)
   ```

2. Create and apply migrations:
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```

Step 3: Define Serializers
1. In `serializers.py` of the `elevators` app, create serializers for Elevator, Floor, and UserRequest models:
   ```python
   # elevators/serializers.py
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
   ```

Step 4: Define ViewSets and API Endpoints
1. In `views.py` of the `elevators` app, create viewsets for Elevator, Floor, and UserRequest models:
   ```python
   # elevators/views.py
   from rest_framework import viewsets
   from rest_framework.response import Response
   from .models import Elevator, Floor, UserRequest
   from .serializers import ElevatorSerializer, FloorSerializer, UserRequestSerializer

   class ElevatorViewSet(viewsets.ModelViewSet):
       queryset = Elevator.objects.all()
       serializer_class = ElevatorSerializer

       def initialize_elevator_system(self, request):
           num_elevators = request.data.get('num_elevators')
           for _ in range(num_elevators):
               Elevator.objects.create()
           return Response({'message': f'{num_elevators} elevators initialized successfully.'})

   class FloorViewSet(viewsets.ModelViewSet):
       queryset = Floor.objects.all()
       serializer_class = FloorSerializer

   class UserRequestViewSet(viewsets.ModelViewSet):
       queryset = UserRequest.objects.all()
       serializer_class = UserRequestSerializer
   ```

2. Configure API endpoints and URL patterns in `urls.py` of the `elevators` app:
   ```python
   # elevators/urls.py
   from django.urls import path, include
   from rest_framework.routers import DefaultRouter
   from .views import ElevatorViewSet, FloorViewSet, UserRequestViewSet

   router = DefaultRouter()
   router.register(r'elevators', ElevatorViewSet, basename='elevators')
   router.register(r'floors', FloorViewSet, basename='floors')
   router.register(r'user-requests', UserRequestViewSet, basename='user-requests')

   urlpatterns = [
       path('', include(router.urls)),
   ]
   ```

3. Add the `elevators` app URLs to the project's main `urls.py`:
   ```python
   # elevator_system/urls.py
   from django.contrib import admin
   from django.urls import path, include

   urlpatterns = [
       path('admin/', admin.site.urls),
       path('api/', include('elevators.urls')),
   ]
   ```

Step 5: Implement Business Logic
1. Implement the business logic in the viewsets to decide which elevator to assign to which floor, mark elevators as available/busy, etc.

Step 6: Test the APIs
1. Run the development server:
   ```
   python manage.py runserver
   ```

2. Use a tool like Postman or cURL to test the APIs:
   - Use the `POST /api/elevators/initialize_elevator_system/` endpoint to initialize the elevators.
   - Use the `GET /api/floors/` endpoint to get all floors and their details.
   - Use the `GET /api/elevators/` endpoint to get all elevators and their details.
   - Use the `GET /api/user-requests/` endpoint to get all user requests and their details.
   - Use the appropriate endpoints to add user requests and perform other elevator actions.

Step 7: Write Documentation
1. Write a well-structured README.md file explaining your design decisions, API contracts, and how to set up, deploy, and test the project.

Step 8: Submission
1. Create a public GitHub repository and push your code to it.
2. Record a short video demonstrating the use of the project and APIs as expected.
3. Share the repository link and video with the provided email address for submission.

Please note that this is a basic outline to help you get started with the project. You may need to add additional logic, error handling, and more advanced features to complete the challenge successfully. Make sure to break down the tasks into smaller steps and implement them one by one. Test your code thoroughly to ensure it works as expected. Good luck with your project!
