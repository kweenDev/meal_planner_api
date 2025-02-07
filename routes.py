"""
Meal Planner Routes
Author: Refiloe Radebe
Date: 2025-01-26
Description: Contains API endpoints for managing meal plans and user authentication.
"""

from flask import request
from flask_restx import Namespace, Resource, fields
from models import db, User, MealPlan
from datetime import datetime
from flask_jwt_extended import (
    create_access_token, jwt_required, get_jwt_identity
)
import logging

logger = logging.getLogger(__name__)

# Define namespaces for authentication and meal planner operations
ns_auth = Namespace('auth', description="Authentication related operations")
ns_mealplanner = Namespace(
    'mealplanner', description="Meal Planner operations")

# API models for documentation
user_model = ns_auth.model('User', {
    'username': fields.String(required=True, description='Username'),
    'email': fields.String(required=True, description='User email'),
    'password': fields.String(required=True, description='User password')
})

login_model = ns_auth.model('Login', {
    'username': fields.String(required=True, description='Username'),
    'password': fields.String(required=True, description='User password')
})

meal_plan_model = ns_mealplanner.model('MealPlan', {
    'userId': fields.String(required=True, description='User ID'),
    'weekStart': fields.String(required=True, description='Week start date (YYYY-MM-DD)'),
    'meals': fields.Raw(required=True, description='Meal plan details in JSON format')
})

update_meal_plan_model = ns_mealplanner.model('UpdateMealPlan', {
    'weekStart': fields.String(required=False, description='Week start date (YYYY-MM-DD)'),
    'meals': fields.Raw(required=False, description='Updated meal plan details in JSON format')
})

# ===============================
# Authentication Endpoints
# ===============================


@ns_auth.route('/register')
class Register(Resource):
    @ns_auth.expect(user_model, validate=True)
    def post(self):
        """
        Register a new user.
        Expected JSON payload:
        {
        "username": "testuser",
        "email": "test@example.com",
        "password": "password"
        }
        Returns:
            JSON response with user data and a success message.
        """
        data = request.json
        if User.query.filter(
            (User.username == data['username']) | (User.email == data['email'])
        ).first():
            return {"message": "User already exists"}, 400
        user = User(username=data['username'], email=data['email'])
        user.set_password(data['password'])
        db.session.add(user)
        db.session.commit()
        return {"message": "User registered successfully", "user": user.to_dict()}, 201


@ns_auth.route('/login')
class Login(Resource):
    @ns_auth.expect(login_model, validate=True)
    def post(self):
        """Authenticate user and return a JWT token."""
        data = request.json
        user = User.query.filter_by(username=data['username']).first()
        if not user or not user.check_password(data['password']):
            return {"message": "Invalid credentials"}, 401
        access_token = create_access_token(identity=user.id)
        return {"message": "Login successful", "access_token": access_token}, 200

# ===============================
# Meal Planner Endpoints
# ===============================


@ns_mealplanner.route('/mealplan')
class MealPlanList(Resource):
    @jwt_required()
    @ns_mealplanner.expect(meal_plan_model, validate=True)
    def post(self):
        """Create a new meal plan."""
        current_user = get_jwt_identity()
        data = request.json
        try:
            meal_plan = MealPlan(
                user_id=current_user,
                week_start=datetime.strptime(data['weekStart'], '%Y-%m-%d'),
                meals=data['meals']
            )
            db.session.add(meal_plan)
            db.session.commit()
            return {
                "message": "Meal plan created successfully",
                "mealPlan": meal_plan.to_dict()
            }, 201
        except Exception as e:
            logger.exception("Error creating meal plan")
            return {
                "message": "An error occurred while creating the meal plan",
                "error": str(e)
            }, 500

    @jwt_required()
    def get(self):
        """Retrieve all meal plans for the current user."""
        current_user = get_jwt_identity()
        meal_plans = MealPlan.query.filter_by(user_id=current_user).all()
        return {"mealPlans": [mp.to_dict() for mp in meal_plans]}, 200


@ns_mealplanner.route('/mealplan/<string:meal_plan_id>')
class MealPlanResource(Resource):
    @jwt_required()
    def get(self, meal_plan_id):
        """Retrieve a specific meal plan by ID."""
        current_user = get_jwt_identity()
        meal_plan = MealPlan.query.filter_by(
            id=meal_plan_id, user_id=current_user).first()
        if not meal_plan:
            return {"message": "Meal plan not found"}, 404
        return {"mealPlan": meal_plan.to_dict()}, 200

    @jwt_required()
    @ns_mealplanner.expect(update_meal_plan_model, validate=True)
    def put(self, meal_plan_id):
        """Update an existing meal plan."""
        current_user = get_jwt_identity()
        meal_plan = MealPlan.query.filter_by(
            id=meal_plan_id, user_id=current_user).first()
        if not meal_plan:
            return {"message": "Meal plan not found"}, 404
        data = request.json
        if 'weekStart' in data:
            meal_plan.week_start = datetime.strptime(
                data['weekStart'], '%Y-%m-%d')
        if 'meals' in data:
            meal_plan.meals = data['meals']
        try:
            db.session.commit()
            return {
                "message": "Meal plan updated successfully",
                "mealPlan": meal_plan.to_dict()
            }, 200
        except Exception as e:
            logger.exception("Error updating meal plan")
            return {
                "message": "An error occurred while updating the meal plan",
                "error": str(e)
            }, 500

    @jwt_required()
    def delete(self, meal_plan_id):
        """Delete an existing meal plan."""
        current_user = get_jwt_identity()
        meal_plan = MealPlan.query.filter_by(
            id=meal_plan_id, user_id=current_user).first()
        if not meal_plan:
            return {"message": "Meal plan not found"}, 404
        try:
            db.session.delete(meal_plan)
            db.session.commit()
            return {"message": "Meal plan deleted successfully"}, 200
        except Exception as e:
            logger.exception("Error deleting meal plan")
            return {
                "message": "An error occurred while deleting the meal plan",
                "error": str(e)
            }, 500
