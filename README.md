# PSG Mock Router

`psg-mock-router` is a lightweight mock API router service designed to simulate routing behavior in an API ecosystem. It helps development, QA, and integration teams by providing a simple, configurable router that returns pre-defined mock responses for different routes and methods.

---

## Table of Contents

- [Overview](#overview)  
- [Features](#features)  
- [Architecture](#architecture)  
- [Tech Stack](#tech-stack)  
- [Directory Structure](#directory-structure)  
- [Getting Started](#getting-started)  
  - [Prerequisites](#prerequisites)  
  - [Installation](#installation)  
  - [Running the Service](#running-the-service)  
- [Configuration](#configuration)  
- [Usage](#usage)  
- [Mock Routes](#mock-routes)  
- [Testing](#testing)  
- [Docker Support](#docker-support)  
- [Contributing](#contributing)  
- [License](#license)  
- [Contact](#contact)  

---

## Overview

`psg-mock-router` acts as a fake HTTP router. You can configure routes (paths + HTTP methods) and response payloads, and the service will listen for incoming requests and respond with mock data. This is especially helpful for:

- Frontend development without a real backend  
- Integration testing with stubbed responses  
- Validating API contracts  
- Simulating different response scenarios (success, error, delay)  

---

## Features

- Define route handlers for different HTTP methods (GET, POST, PUT, DELETE, etc.)  
- Return custom JSON responses for each route  
- Support for response status codes and headers  
- Easy-to-extend handler logic  
- Lightweight and minimal overhead  
- Containerizable via Docker for easy deployment  

---

## Architecture

┌───────────────────────────┐
│ Client / Frontend / API │
└─────────────┬─────────────┘
│ HTTP Request to mock router
▼
┌───────────────────────────┐
│ PSG Mock Router │
│ - Matches path & method │
│ - Returns configured mock│
├───────────────────────────┤
│ Response (JSON + status)│
└───────────────────────────┘

yaml

---

## Tech Stack

- **Language:** Python  
- **Framework:** Flask / FastAPI / other lightweight HTTP server (adapt based on your code)  
- **Configuration:** JSON or Python objects for defining routes  
- **Containerization:** Docker (optional)  

---

## Directory Structure

Here’s a typical layout for this service (adjust according to your repo):

psg-mock-router/
├── main.py # Entry point to run the mock router
├── routes/ # Route definitions or handlers
├── config/ # Config files for routes, responses
├── utils/ # Utility functions (e.g. delay, logging)
├── requirements.txt # Python dependencies
└── Dockerfile # Dockerfile to containerize the mock service

yaml

---

## Getting Started

### Prerequisites

- Python 3.7+  
- `pip`  
- Docker (optional, for containerized runs)  

### Installation

1. Clone the repo:

   ```bash
   git clone https://github.com/simpsonorg/psg-mock-router.git
   cd psg-mock-router
(Optional) Create a virtual environment:

bash
python3 -m venv venv
source venv/bin/activate
Install dependencies:

bash
pip install -r requirements.txt
Running the Service
Start the mock router:

bash
python main.py
This will launch the HTTP server; by default, it listens on a port defined in the configuration (or main.py).

Configuration
You configure mock routes by editing a config file (e.g., JSON or Python dict) in the config/ folder. Typical configuration options:

Path: The URL path to mock (e.g. /api/users)

Method: HTTP method (GET, POST, PUT, DELETE)

Response Body: JSON or other payload to return

Status Code: HTTP status code for the response

Headers: Optional response headers

Delay: Optional delay in response (simulate network latency)

Example config (in JSON):

json
Copy code
{
  "/api/users": {
    "GET": {
      "status": 200,
      "response": [
        { "id": 1, "name": "Alice" },
        { "id": 2, "name": "Bob" }
      ]
    },
    "POST": {
      "status": 201,
      "response": { "id": 3, "name": "Charlie" }
    }
  }
}
Usage
Once the service is running, you can send HTTP requests to your mock endpoints just like you would a real API:

bash
curl http://localhost:5000/api/users
curl -X POST http://localhost:5000/api/users -H "Content-Type: application/json" -d '{"name": "Charlie"}'
The mock router will match the request against its configured routes, and send the predefined mock response.

Mock Routes
Define all the routes, methods, and responses in the config. Some use-cases:

GET /resources → return a list of resources

GET /resources/{id} → return a specific item

POST /resources → accept a JSON body and respond with a created resource

PUT /resources/{id} → update an existing resource

DELETE /resources/{id} → simulate deletion

You can also configure error scenarios (e.g., 400, 500) or add custom headers and delays.

Testing
Use pytest to write tests for your mock routes.

Use Flask’s test client / FastAPI’s test client to simulate requests and validate responses.

Test edge cases such as non-configured routes, invalid request methods, and simulated error responses.

Example (pytest + Flask):

python
def test_get_users(client):
    response = client.get("/api/users")
    assert response.status_code == 200
    data = response.json
    assert isinstance(data, list)
Docker Support
To run the mock router in Docker:

Build the Docker image:

bash
docker build -t psg-mock-router .
Run the container:

bash
docker run -p 5000:5000 psg-mock-router
If your config depends on environment variables, you can pass them:

bash
docker run -e ROUTES_CONFIG=config/routes.json -p 5000:5000 psg-mock-router
Contributing
Contributions are welcome! Here’s how to contribute:

Fork the repository

Create a new branch: git checkout -b feature/my-mock-route

Add or update route configurations, handler logic, or tests

Commit your changes: git commit -m "Add mock route for /api/foo"

Push your branch: git push origin feature/my-mock-route

Create a Pull Request

License
This project is licensed under the Citi License.
