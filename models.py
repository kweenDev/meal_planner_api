"""
Meal Planner Models
Author: Refiloe Radebe
Date: 2025-01-25
Description: Contains SQLAlchemy models for handling users and meal plans.
"""

from datetime import datetime
import uuid
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

# Create the SQLAlchemy database instance
db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.String(36), primary_key=True,
                   default=lambda: str(uuid.uuid4()))
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    # Updated column length for password_hash to 256
    password_hash = db.Column(db.String(256), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def set_password(self, password):
        """Hashes and sets the user's password."""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """Checks if the provided password matches the stored hash."""
        return check_password_hash(self.password_hash, password)

    def to_dict(self):
        """Returns a dictionary representation of the user."""
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "createdAt": self.created_at.strftime("%Y-%m-%d %H:%M:%S") if self.created_at else None
        }


class MealPlan(db.Model):
    __tablename__ = 'meal_plans'

    id = db.Column(db.String(36), primary_key=True,
                   default=lambda: str(uuid.uuid4()))
    user_id = db.Column(db.String(36), db.ForeignKey(
        'users.id'), nullable=False)
    week_start = db.Column(db.Date, nullable=False)
    meals = db.Column(db.JSON, nullable=False)  # Storing meal details as JSON
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)

    # Relationship to the User model
    user = db.relationship('User', backref=db.backref('meal_plans', lazy=True))

    def to_dict(self):
        """Returns a dictionary representation of the meal plan."""
        return {
            "id": self.id,
            "userId": self.user_id,
            "weekStart": self.week_start.strftime("%Y-%m-%d"),
            "meals": self.meals,
            "createdAt": self.created_at.strftime("%Y-%m-%d %H:%M:%S") if self.created_at else None,
            "updatedAt": self.updated_at.strftime("%Y-%m-%d %H:%M:%S") if self.updated_at else None
        }
