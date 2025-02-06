"""
Meal Planner API
Author: Refiloe Radebe
Date: 2025-01-25
Description: Entry point for the Meal Planner API built with Flask, SQLAlchemy, and JWT Authentication.
"""

import logging
from flask import Flask
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_restx import Api
from flask_cors import CORS
from config import Config
from models import db  # db is defined in models.py


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Set up logging
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    # Initialize the database and migrations
    db.init_app(app)
    Migrate(app, db)

    # Initialize JWT
    JWTManager(app)

    # Set up API documentation using Flask-RESTX
    api = Api(
        app,
        version="1.0",
        title="Meal Planner API",
        description="API for managing meal plans with user authentication",
        doc="/docs"
    )

    # Import and add namespaces for authentication and meal planner routes
    from routes import ns_auth, ns_mealplanner
    api.add_namespace(ns_auth, path="/api/v1/auth")
    api.add_namespace(ns_mealplanner, path="/api/v1/meal-planner")

    return app


# Create the global app instance for development
app = create_app()
CORS(app)

if __name__ == '__main__':
    app.run(debug=True)
