"""
Config File
Author: Refiloe Radebe
Date: 2025-01-25
Description: Configuration settings for the Meal Planner API.
"""

import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()


class Config:
    DEBUG = True
    SECRET_KEY = os.getenv("SECRET_KEY", "my_super_secret_flask_key")
    # PostgreSQL connection string using your provided credentials
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL",
        "postgresql://meal_planner_user:YOUR_DB_PASSWORD@localhost:5432/mealplanner_api_db"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "my_super_secret_jwt_key")
