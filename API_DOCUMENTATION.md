
# Meal Planner API Documentation

**Version:** 1.0  
**Author:** Refiloe Radebe  
**Last Updated:** 2025-02-06

---

## Overview

The Meal Planner API is a RESTful service built with Flask, SQLAlchemy, PostgreSQL, and JWT for secure authentication. It allows users to register, log in, and manage meal plans (create, read, update, delete). Interactive documentation is available at the `/docs` endpoint.

---

## Base URL

- **Development:** `http://localhost:5000/api/v1`
- **Production:** `http://<your-domain>/api/v1`

---

## Environment Variables

The API uses the following environment variables:

- **SECRET_KEY:** A secret key for Flask sessions.
- **JWT_SECRET_KEY:** A secret key for signing JWT tokens.
- **DATABASE_URL:** PostgreSQL connection string (e.g., `postgresql://meal_planner_user:admin2@localhost:5432/mealplanner_api_db`).

*Note: For production, ensure that sensitive information is securely set via environment variables.*

---

## Endpoints

### Authentication

#### User Registration**

- **URL:** `/api/v1/auth/register`
- **Method:** `POST`
- **Description:** Registers a new user.
- **Request Body:**

  ```json
  {
    "username": "testuser",
    "email": "test@example.com",
    "password": "password"
  }
   ```

- **Error Response:**
  - **Code:** `400 Bad Request`

#### User Login

- **URL:** `/api/v1/auth/login`
- **Method:** `POST`
- **Description:** Authenticates a user and returns a JWT token.
- **Request Body:**

    ```json
    {
        "username": "testuser",
        "password": "password"
    }
    ```

- **Success Response:**
  - **Code:** `200 OK`
  - **Body:**

    ```json
    {
        "message": "Login successful",
        "access_token": "<jwt-token>"
    }
    ```

- **Error Response:**
  - **Code:** `401 Unauthorized`

---

### Meal Planner Operations

*All endpoints require JWT authentication via the `Authorization: Bearer <token>` header.*

#### Create a Meal Plan

- **URL:** `/api/v1/meal-planner/mealplan`
- **Method:** `POST`
- **Description:** Creates a new meal plan for the authenticated user.
- **Request Body:**

    ```json
    {
        "userId": "ignored_in_backend",
        "weekStart": "YYYY-MM-DD","meals": {
            "Monday": ["Breakfast", "Lunch", "Dinner"],
            "Tuesday": ["Snack", "Lunch", "Dinner"]
            }
    }
    ```

- **Success Response:**
  - **Code:** `201 CREATED`
  - **Body:** Contains the meal plan object.
- **Error Response:**
  - **Code:** `40 Bad Request` or `500 Internal Server Error`

#### Get a Meal Plan

- **URL:** `/api/v1/meal-planner/mealplan/<meal_plan_id>`
- **Method:** `GET`
- **Description:** Retrieves a specific meal plan for the authenticated user.
- **Success Response:**
  - **Code:** `200 OK`
  - **Body:** Contains the meal plan object.
- **Error Response:**
  - **Code:** `404 Not Found`

#### Update a Meal Plan

- **URL:** `/api/v1/meal-planner/mealplan/<meal_plan_id>`
- **Method:** `PUT`
- **Description:** Updates an existing meal plan.
- **Request Body:**

    ```json
    {
        "weekStart": "YYYY-MM-DD","meals": {
            "Monday": ["Updated Breakfast", "Updated Lunch", "Updated Dinner"],
            "Tuesday": ["Updated Snack", "Updated Lunch", "Updated Dinner"]
            }
    }
    ```

- **Success Response:**
  - **Code:** `200 OK`
  - **Body:** Contains the updated meal plan object.
- **Error Response:**
  - **Code:** `404 Not Found` or `500 Internal Server Error`

#### Delete a Meal Plan

- **URL:** `/api/v1/meal-planner/mealplan/<meal_plan_id>`
- **Method:** `DELETE`
- **Description:** Deletes a meal plan.
- **Success Response:**
  - **Code:** `200 OK`
  - **Body:**

    ```json
    {
        "message": "Meal plan deleted successfully"
    }
    ```

- **Error Response:**
  - **Code:** `404 Not Found` or `500 Internal Server Error`

---

## Additional Information

- **Interactive Documentation:**
Visit `/docs` on your backend server to view the interactive Swagger UI.
- **Error Handling:**
The API uses standard HTTP status codes and provides error messages in the response body.

---

## Conclusion

This API documentation provides all the details necessary to interact with the Meal Planner API. For any further information or troubleshooting, refer to the source code and inline comments.

Happy coding, and thank you for using the Meal Planner API!
