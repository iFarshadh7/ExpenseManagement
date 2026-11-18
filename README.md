# Expense Management API

A simple RESTful API built with **FastAPI** for managing personal expenses. This project demonstrates CRUD operations using an in-memory Python dictionary without requiring a database.

## Features

- Create a new expense.
- Retrieve all expenses.
- Retrieve a specific expense by ID.
- Update an existing expense.
- Delete an expense.
- Automatic input validation using Pydantic.
- HTTP error handling for non-existent expenses.
- Interactive API documentation with Swagger UI.

## Technologies Used

- Python
- FastAPI
- Pydantic
- Uvicorn

## Project Structure

```text
ExpenseManagement/
│
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/iFarshadh7/ExpenseManagement.git
cd ExpenseManagement
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

**Windows:**

```powershell
.venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

## Run the Application

Start the FastAPI development server:

```bash
uvicorn main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

## API Documentation

FastAPI automatically generates interactive API documentation.

- **Swagger UI:** http://127.0.0.1:8000/docs
- **ReDoc:** http://127.0.0.1:8000/redoc

## API Endpoints

| HTTP Method | Endpoint | Description |
|---|---|---|
| POST | `/expenses/` | Create a new expense |
| GET | `/expenses/` | Retrieve all expenses |
| GET | `/expenses/{expense_id}` | Retrieve an expense by ID |
| PUT | `/expenses/{expense_id}` | Update an existing expense |
| DELETE | `/expenses/{expense_id}` | Delete an expense |

## Example Request

Create a new expense:

**POST** `/expenses/`

Request body:

```json
{
  "description": "Buying a book",
  "amount": 250000
}
```

Example response:

```json
{
  "id": 1,
  "description": "Buying a book",
  "amount": 250000.0
}
```

## HTTP Status Codes

| Status Code | Description |
|---|---|
| 200 | OK |
| 201 | Created |
| 204 | No Content |
| 404 | Expense Not Found |
| 422 | Validation Error |

## Data Storage

This project uses a Python dictionary as an in-memory data store.

**Note:** All expense records are temporary and will be lost when the application stops or restarts. No database is used in this project.

## Project Branch

The exercise is developed in the following Git branch:

```text
feature/expense-management-api
```

## Learning Objectives

This project was developed as a practical exercise to learn:

- RESTful API development with FastAPI.
- CRUD operations.
- Pydantic models and data validation.
- HTTP methods and status codes.
- Basic API error handling.
- Git and GitHub branch management.

---

**Author:** [iFarshadh7](https://github.com/iFarshadh7)

**Project:** [ExpenseManagement](https://github.com/iFarshadh7/ExpenseManagement)
