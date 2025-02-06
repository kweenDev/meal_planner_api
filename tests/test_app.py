"""
Meal Planner API Tests
Author: Refiloe Radebe
Date: 2025-01-25
Description: Test cases for the Meal Planner API with authentication.
"""

import json
import pytest
from app import create_app, db
from tests.test_config import TestConfig


@pytest.fixture
def client():
    """
    Pytest fixture for creating a test client with an in-memory database.

    Returns:
        FlaskClient: The Flask test client.
    """
    app = create_app(TestConfig)
    with app.app_context():
        db.create_all()
        yield app.test_client()
        db.drop_all()


def register_user(client, username="testuser", email="test@example.com", password="password"):
    """
    Helper function to register a new user.
    """
    payload = {
        "username": username,
        "email": email,
        "password": password
    }
    return client.post(
        '/api/v1/auth/register',
        data=json.dumps(payload),
        content_type='application/json'
    )


def login_user(client, username="testuser", password="password"):
    """
    Helper function to log in a user and return the access token.
    """
    payload = {
        "username": username,
        "password": password
    }
    return client.post(
        '/api/v1/auth/login',
        data=json.dumps(payload),
        content_type='application/json'
    )


def test_user_registration_and_login(client):
    """
    Test user registration and login.
    """
    # Register a new user
    reg_response = register_user(client)
    reg_data = json.loads(reg_response.data)
    assert reg_response.status_code == 201, f"Registration failed: {reg_data}"
    assert reg_data["message"] == "User registered successfully"

    # Log in with the registered user
    login_response = login_user(client)
    login_data = json.loads(login_response.data)
    assert login_response.status_code == 200, f"Login failed: {login_data}"
    assert "access_token" in login_data


def test_create_and_get_meal_plan(client):
    """
    Test creating a meal plan and retrieving it.
    """
    # Register and log in to get an access token
    register_user(client)
    login_response = login_user(client)
    login_data = json.loads(login_response.data)
    token = login_data["access_token"]

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    # Create a new meal plan
    payload = {
        "userId": "ignored_in_backend",  # Backend uses JWT identity instead
        "weekStart": "2025-02-10",
        "meals": {
            "Monday": ["Breakfast", "Lunch", "Dinner"],
            "Tuesday": ["Snack", "Lunch", "Dinner"]
        }
    }
    create_response = client.post(
        '/api/v1/meal-planner/mealplan',
        data=json.dumps(payload),
        headers=headers
    )
    create_data = json.loads(create_response.data)
    assert create_response.status_code == 201, f"Meal plan creation failed: {create_data}"
    assert create_data["message"] == "Meal plan created successfully"
    meal_plan_id = create_data["mealPlan"]["id"]

    # Retrieve the created meal plan
    get_response = client.get(
        f'/api/v1/meal-planner/mealplan/{meal_plan_id}',
        headers=headers
    )
    get_data = json.loads(get_response.data)
    assert get_response.status_code == 200, f"Meal plan retrieval failed: {get_data}"
    assert get_data["mealPlan"]["id"] == meal_plan_id


def test_update_and_delete_meal_plan(client):
    """
    Test updating and deleting a meal plan.
    """
    # Register and log in to get an access token
    register_user(client)
    login_response = login_user(client)
    token = json.loads(login_response.data)["access_token"]

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    # Create a new meal plan
    payload = {
        "userId": "ignored",
        "weekStart": "2025-02-10",
        "meals": {
            "Monday": ["Breakfast", "Lunch", "Dinner"],
            "Tuesday": ["Snack", "Lunch", "Dinner"]
        }
    }
    create_response = client.post(
        '/api/v1/meal-planner/mealplan',
        data=json.dumps(payload),
        headers=headers
    )
    create_data = json.loads(create_response.data)
    meal_plan_id = create_data["mealPlan"]["id"]

    # Update the meal plan
    update_payload = {
        "weekStart": "2025-02-17",
        "meals": {
            "Monday": ["Updated Breakfast", "Updated Lunch", "Updated Dinner"],
            "Tuesday": ["Updated Snack", "Updated Lunch", "Updated Dinner"]
        }
    }
    update_response = client.put(
        f'/api/v1/meal-planner/mealplan/{meal_plan_id}',
        data=json.dumps(update_payload),
        headers=headers
    )
    update_data = json.loads(update_response.data)
    assert update_response.status_code == 200, f"Meal plan update failed: {update_data}"
    assert update_data["mealPlan"]["weekStart"] == "2025-02-17"

    # Delete the meal plan
    delete_response = client.delete(
        f'/api/v1/meal-planner/mealplan/{meal_plan_id}',
        headers=headers
    )
    delete_data = json.loads(delete_response.data)
    assert delete_response.status_code == 200, f"Meal plan deletion failed: {delete_data}"
    assert delete_data["message"] == "Meal plan deleted successfully"
