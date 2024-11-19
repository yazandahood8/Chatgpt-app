
# Flask Backend Project with PostgreSQL and OpenAI Integration

![Flask + PostgreSQL](https://upload.wikimedia.org/wikipedia/commons/3/3c/Flask_logo.svg)
![PostgreSQL](https://upload.wikimedia.org/wikipedia/commons/2/29/Postgresql_elephant.svg)

## Overview

This project is a backend application developed with Flask and PostgreSQL that interacts with the OpenAI API to answer user-submitted questions. It includes Docker support, database migrations using Alembic, and comprehensive test coverage with Pytest. The project has been set up with Docker for easy deployment and PostgreSQL as the database.

---

### Table of Contents
1. [Overview](#overview)
2. [Key Features](#key-features)
3. [Tech Stack](#tech-stack)
4. [Getting Started](#getting-started)
   - [Prerequisites](#prerequisites)
   - [Installation](#installation)
   - [Environment Variables](#environment-variables)
   - [Running the Application](#running-the-application)
   - [Running Tests](#running-tests)
5. [Project Structure](#project-structure)
6. [API Endpoints](#api-endpoints)
7. [Screenshots](#screenshots)
8. [Contributing](#contributing)
9. [License](#license)

---

## Key Features

- **Flask**: Lightweight Python web framework.
- **PostgreSQL**: Powerful, open-source object-relational database.
- **Docker**: Containerized setup for seamless deployment.
- **Alembic Migrations**: Database schema migrations.
- **Pytest**: Unit testing with test cases covering most of the functionality.
- **OpenAI Integration**: Uses the OpenAI API to answer questions.

---

## Tech Stack

- **Backend**: Flask (Python)
- **Database**: PostgreSQL
- **Containerization**: Docker
- **Testing**: Pytest
- **Migrations**: Alembic
- **API**: OpenAI GPT-3.5 Turbo

---

## Getting Started

### Prerequisites

- Docker installed on your machine
- Python 3.8+ installed locally for running Flask outside Docker (optional)
- PostgreSQL or a Dockerized database for local development

### Installation

1. **Clone the repository**:

   ```bash
   git clone <https://github.com/yazandahood8/Flask-Backend-Project.git>
   cd backend_project
   ```

2. **Install dependencies** (if running locally):

   ```bash
   pip install -r requirements.txt
   ```

### Environment Variables

Create a `.env` file in the root of the project to store your environment variables.

```env
DATABASE_URL=postgresql://postgres:password@db:5432/dbname
OPENAI_API_KEY=your-openai-api-key
```

### Running the Application

1. **Start the Docker containers**:

   ```bash
   docker-compose up --build
   ```

   This will spin up both the Flask app and the PostgreSQL database using Docker.

2. **Run database migrations**:

   ```bash
   docker exec -it <flask-container-name> flask db upgrade
   ```

3. **Access the application**: Visit `http://localhost:5000` in your browser.

### Running Tests

Run the tests with Pytest to ensure the application is working as expected:

```bash
docker exec -it <flask-container-name> pytest
```

---

## Project Structure

```bash
backend_project/
│
├── Dockerfile                # Dockerfile for the Flask app
├── docker-compose.yml        # Docker Compose setup for Flask + PostgreSQL
├── requirements.txt          # Python dependencies
├── app.py                    # Main Flask application
├── models.py                 # Database models
├── services.py               # Service logic (e.g., OpenAI integration)
├── config.py                 # Configuration for the application
├── migrations/               # Alembic migrations
├── test_app.py               # Pytest test cases
└── README.md                 # This file
```

---

## API Endpoints

### `/ask` [POST]

- **Description**: Accepts a question and returns an AI-generated answer using OpenAI GPT-3.5 Turbo.
- **Payload**:

```json
{
  "question": "What is AI?"
}
```

- **Response**:

```json
{
  "question": "What is AI?",
  "answer": "AI stands for Artificial Intelligence."
}
```

- **Errors**:
  - `400`: When the question is missing.
  - `429`: When OpenAI quota is exceeded.
  - `500`: Internal Server Error.

---

## Screenshots

### 1. **Postman Request for `/ask` Endpoint**

![Postman](https://github.com/yazandahood8/Flask-Backend-Project/blob/main/postman.png)

### 2. **Docker Compose Up**

![Docker Compose](https://github.com/yazandahood8/Flask-Backend-Project/blob/main/docker.png)

### 3. **PostgreSQL database**

![PostgreSQL database](https://github.com/yazandahood8/Flask-Backend-Project/blob/main/sql.png)

---

## Contributing

Contributions are welcome! If you have any ideas or feedback, feel free to submit an issue or a pull request.

---



### Contact Information

For any queries or additional questions, feel free to contact me on [LinkedIn](https://www.linkedin.com/in/yazan-dahood-031145309/).
