"""
Test Configuration
Author: Refiloe Radebe
Date: 2025-02-06
Description: Testing configuration for the Meal Planner API.
"""


class TestConfig:
    TESTING = True
    SECRET_KEY = "test-secret-key"
    # Use in-memory SQLite for testing
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = "test-jwt-secret"
