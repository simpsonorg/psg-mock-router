# PSG Mock Router

`psg-mock-router` is a lightweight Python-based mock API router service. It is designed to simulate routing behavior for APIs, helping development and QA teams mock backend responses without relying on real backend APIs.

## Table of Contents

- [Motivation](#motivation)  
- [Features](#features)  
- [Architecture](#architecture)  
- [Getting Started](#getting-started)  
  - [Prerequisites](#prerequisites)  
  - [Installation](#installation)  
  - [Running](#running)  
  - [Configuration](#configuration)  
- [Usage](#usage)  
- [Examples](#examples)  
- [Testing](#testing)  
- [Contributing](#contributing)  
- [License](#license)  
- [Contact](#contact)  

---

## Motivation

When building distributed systems or microservices, frontend developers, integration testers, and QA teams often need stable, predictable API endpoints before the real backend is ready. `psg-mock-router` allows you to:

- Mock API routes and return predefined responses  
- Simulate API behavior (status codes, headers, payloads)  
- Run a lightweight router locally or in a container for faster development feedback  

---

## Features

- HTTP mock server implemented in Python (`main.py`)  
- Configurable routing logic to respond to different endpoints  
- Ability to mock different HTTP methods (GET, POST, etc.)  
- Return JSON or other payloads as responses  
- Docker support for containerized deployment  
- Easy to extend for custom mock behaviors  

---

## Architecture

1. **Python Application**  
   The core logic is in `main.py`. It handles incoming HTTP requests and dispatches them to matching mock route handlers.  
2. **Routing Logic**  
   You define mock routes (path + method) and corresponding response payloads in the code or configuration.  
3. **Docker**  
   A `Dockerfile` is included, so you can build an image and run the service in containerized environments.  
4. **Lightweight**  
   The service is intentionally kept minimal so it’s easy to maintain and extend.

---

## Getting Started

### Prerequisites

- Python 3.7+  
- `pip` (or `venv`)  
- Docker (optional, if you want to run via Docker)  

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/simpsonorg/psg-mock-router.git
   cd psg-mock-router
(Optional but recommended) Create a virtual environment:

2.python3 -m venv venv
source venv/bin/activate

3.Install dependencies:
pip install -r requirements.txt

