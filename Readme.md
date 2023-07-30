# Elevator System Project

![Elevator System](https://example.com/path/to/elevator_image.png)

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Assumptions](#assumptions)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

## Introduction
The Elevator System is a simplified elevator model built using Python and Django. It allows you to create and manage elevators, floors, and user requests. This project is an API-based solution that can be integrated into various applications.

## Features
- Initialize the elevator system with 'n' elevators.
- Fetch all requests for a given elevator.
- Fetch the next destination floor for a given elevator.
- Determine if the elevator is moving up or down currently.
- Save user requests to the list of requests for an elevator.
- Mark an elevator as not working or in maintenance.
- Open and close the elevator door.

## Assumptions
- Each elevator can move up and down, open and close its door, start and stop running.
- The elevator system assigns the most optimal elevator to a user based on their request.
- The system has one button per floor for requesting the elevator.
- Elevator movement happens instantly when the API is called.
- The system uses Django and Django Rest Framework for API development.

## Requirements
- Python 3.x
- Django
- Django Rest Framework
- Postgres (optional, if you want to use it as the database)
- Redis (optional, for caching)

## Installation
1. Clone the repository:


Installation
------------
1. Clone the repository:
   ```
   git clone https://github.com/your-username/elevator-system.git
   cd elevator-system
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

3. Configure the database (if using Postgres):
   - Create a new Postgres database and update the database settings in `settings.py`.

4. Run the migrations:
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Create a superuser (optional, for accessing Django admin):
   ```
   python manage.py createsuperuser
   ```

6. Start the development server:
   ```
   python manage.py runserver
   ```

Usage
-----
1. Initialize the elevator system with 'n' elevators:
   - Send a POST request to `/api/elevators/initialize_elevator_system/` with the number of elevators as JSON data.

2. Access the Django admin (optional):
   - Visit `http://localhost:8000/admin/` and log in with the superuser credentials.

3. Use the provided API endpoints to manage elevators, floors, and user requests.

API Endpoints
-------------
- Initialize Elevator System:
  - `POST /api/elevators/initialize_elevator_system/`
  - Request Data: `{ "num_elevators": 3 }`
  - Response Data: `{ "message": "3 elevators initialized successfully." }`

- Get All Elevators:
  - `GET /api/elevators/`
  - Response Data: `[ { "id": 1, "operational": true }, { "id": 2, "operational": true } ]`

- Get All Floors:
  - `GET /api/floors/`
  - Response Data: `[ { "id": 1, "number": 1 }, { "id": 2, "number": 2 } ]`

- Get All User Requests:
  - `GET /api/user-requests/`
  - Response Data: `[ { "id": 1, "floor": 2, "direction": "UP" }, { "id": 2, "floor": 5, "direction": "DOWN" } ]`

- Add User Request:
  - `POST /api/user-requests/`
  - Request Data: `{ "floor": 3, "direction": "UP" }`
  - Response Data: `{ "id": 3, "floor": 3, "direction": "UP" }`

- Fetch Next Destination Floor for Elevator:
  - `GET /api/elevators/1/next-destination/`
  - Response Data: `{ "next_floor": 4, "direction": "UP" }`

- Mark Elevator as Not Working:
  - `PATCH /api/elevators/1/mark-not-working/`
  - Response Data: `{ "message": "Elevator 1 marked as not working." }`

- Open/Close Elevator Door:
  - `PATCH /api/elevators/1/open-door/`
  - Response Data: `{ "message": "Elevator 1 door opened." }`
  - `PATCH /api/elevators/1/close-door/`
  - Response Data: `{ "message": "Elevator 1 door closed." }`

Testing
-------
To test the existing code and API endpoints, you can use the `curl` command-line tool or other API testing tools like Postman or Insomnia. Let's go through some examples of how to test the API endpoints:

1. Initialize Elevator System:
   Send a POST request to initialize the elevator system with 'n' elevators. For example, to initialize 3 elevators, you can use the following `curl` command:

   ```bash
   curl -X POST http://localhost:8000/api/elevators/initialize_elevator_system/ -H "Content-Type: application/json" -d '{"num_elevators": 3}'
   ```

2. Get All Elevators:
   To fetch all elevators, send a GET request to the following endpoint:

   ```bash
   curl -X GET http://localhost:8000/api/elevators/
   ```

3. Get All Floors:
   To fetch all floors, send a GET request to the following endpoint:

   ```bash
   curl -X GET http://localhost:8000/api/floors/
   ```

4. Get All User Requests:
   To fetch all user requests, send a GET request to the following endpoint:

   ```bash
   curl -X GET http://localhost:8000/api/user-requests/
   ```

5. Add User Request:
   To add a user request, send a POST request with the floor number and direction as JSON data. For example:

   ```bash
   curl -X POST http://localhost:8000/api/user-requests/ -H "Content-Type: application/json" -d '{"floor": 3, "direction": "UP"}'
   ```

6. Fetch Next Destination Floor for Elevator:
   To get the next destination floor for a specific elevator (here, the elevator with ID 1), send a GET request as follows:

   ```bash
   curl -X GET http://localhost:8000/api/elevators/1/next-destination/
   ```

7. Mark Elevator as Not Working:
   To mark an elevator (here, the elevator with ID 1) as not working, send a PATCH request:

   ```bash
   curl -X PATCH http://localhost:8000/api/elevators/1/mark-not-working/
   ```

8. Open/Close Elevator Door:
   To open or close the door of an elevator (here, the elevator with ID 1), send PATCH requests as follows:

   ```bash
   curl -X PATCH http://localhost:8000/api/elevators/1/open-door/
   curl -X PATCH http://localhost:8000/api/elevators/1/close-door/
   ```

Note: Make sure to replace `http://localhost:8000/` with the appropriate URL if your server is running on a different host or port.

After sending these `curl` commands, you should receive responses from the server indicating the success or failure of the operations. The responses will contain the relevant data, such as elevator details, floor details, user request details, etc.

You can also use tools like Postman or Insomnia to test the API endpoints interactively with a more user-friendly interface


Contributing
------------
Contributions are welcome! If you find any issues or have ideas for improvements, feel free to open an issue or submit a pull request.

License
-------
This project is licensed under the MIT License - see the LICENSE file for details.
```
