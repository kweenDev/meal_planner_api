
# Meal Planner API & Frontend Application

**Author:** Refiloe Radebe  
**Date:** 2025-02-06

---

## Overview

The Meal Planner project is a full-stack web application that allows users to register, log in, and manage their weekly meal plans. The backend is built using Flask, SQLAlchemy, PostgreSQL, and JWT for authentication, while the frontend is developed with React, Axios, React Router, and Bootstrap for a responsive and user-friendly interface.

Interactive API documentation is available via Swagger UI at the `/docs` endpoint when the backend is running.

---

## Features

- **User Authentication:**  
  - Secure user registration and login using JWT.
- **Meal Plan Management:**  
  - Create, read, update, and delete meal plans.
- **Responsive Frontend:**  
  - Mobile-friendly design using Bootstrap.
- **API Documentation:**  
  - Interactive documentation powered by Flask-RESTX.
- **Environment Configuration:**  
  - Sensitive data (e.g., JWT secret, database URL) managed via environment variables.

---

## Technologies Used

- **Backend:**  
  - Python, Flask, Flask-Migrate, Flask-JWT-Extended, Flask-RESTX, SQLAlchemy, PostgreSQL
- **Frontend:**  
  - React, Axios, React Router DOM, Bootstrap
- **Tooling:**  
  - Webpack, npm, concurrently

---

## Installation & Setup

### Prerequisites

- **Backend:**  
  - Python 3.11+, PostgreSQL
- **Frontend:**  
  - Node.js and npm

### Backend Setup

1. **Clone the repository** and navigate to the backend directory:

   ```bash
   cd meal_planner_api
   ```

2. **Create a virtual environment** and activate it:

    ```bash
    python -m venv venv
    # Windows:
    venv\Scripts\activate
    # macOS/Linux:
    source venv/bin/activate
    ```

3. **Install the dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Set environment variables**:
Create a `.env` file in the backend root (or set these variables in your environment):

    ```dotenv
    SECRET_KEY=your_super_secret_flask_key
    JWT_SECRET_KEY=your_super_secret_jwt_key
    DATABASE_URL=postgresql://meal_planner_user:admin2@localhost:5432/mealplanner_api_db
    ```

    *(Note: For production, do not hard-code credentials. Use secure methods to set environment variables.)*

5. **Initialise and upgrade the database using Flask-Migrate**:

    ```bash
    flask db init
    flask db migrate -m "Initial migration"
    flask db upgrade
    ```

6. **Run the backend**:

    ```bash
    flask run
    ```

---

### Frontend Setup

1. **Navigate to the frontend directory**:

    ```bash
    cd meal-planner-frontend
    ```

2. **Install Node.js dependencies**:

    ```bash
    npm install
    ```

3. **Run the frontend**:

    ```bash
    npm start
    ```

---

### Running Both Servers Simultaneously

If you want to run both servers concurrently, use the provided script in the `meal-planner-frontend` directory:

1. Open your **meal-planner-frontend/package.json** and ensure the `"backend"` script is correctly set:

    ```json
    "scripts": {
        "start": "react-scripts start",
        "backend": "python ../app.py",
        "dev": "concurrently \"npm run backend\" \"npm start\""
        }
    ```

2. From the **meal-planner-frontend** directory, run:

    ```bash
    npm run dev
    ```
