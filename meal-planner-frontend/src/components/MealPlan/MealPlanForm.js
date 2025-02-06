/**
 * MealPlanForm.js
 * Author: Refiloe Radebe
 * Date: 2025-02-06
 * Description: Component for creating a new meal plan.
 */

import React, { useState } from 'react';
import API from '../../services/api';

/**
 * MealPlanForm component renders a form to create a meal plan.
 * @param {Function} onSuccess - Callback invoked after successful submission.
 * @returns {JSX.Element} The meal plan creation form.
 */
const MealPlanForm = ({ onSuccess }) => {
  const [weekStart, setWeekStart] = useState('');
  const [meals, setMeals] = useState({}); // Expected format: { Monday: [...], Tuesday: [...] }
  const [message, setMessage] = useState('');

  /**
   * Handles changes for meal inputs for a given day.
   * @param {string} day - The day of the week.
   * @param {Object} e - The change event.
   */
  const handleMealChange = (day, e) => {
    // Convert comma-separated string to array
    const value = e.target.value.split(',').map((item) => item.trim());
    setMeals({ ...meals, [day]: value });
  };

  /**
   * Handles form submission.
   * @param {Object} e - The form submission event.
   */
  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const payload = { weekStart, meals };
      const response = await API.post('/meal-planner/mealplan', payload);
      setMessage(response.data.message);
      if (onSuccess) onSuccess();
    } catch (error) {
      setMessage(error.response?.data?.message || 'Submission failed');
    }
  };

  return (
    <div className="card my-4">
      <div className="card-body">
        <h3>Create New Meal Plan</h3>
        {message && <div className="alert alert-info">{message}</div>}
        <form onSubmit={handleSubmit}>
          <div className="form-group">
            <label htmlFor="weekStart">Week Start Date (YYYY-MM-DD):</label>
            <input
              type="date"
              id="weekStart"
              className="form-control"
              value={weekStart}
              onChange={(e) => setWeekStart(e.target.value)}
              required
            />
          </div>
          {/* For demonstration, inputs for Monday and Tuesday */}
          <div className="form-group mt-2">
            <label htmlFor="monday">Monday Meals (comma-separated):</label>
            <input
              type="text"
              id="monday"
              className="form-control"
              onChange={(e) => handleMealChange('Monday', e)}
              placeholder="e.g., Breakfast, Lunch, Dinner"
            />
          </div>
          <div className="form-group mt-2">
            <label htmlFor="tuesday">Tuesday Meals (comma-separated):</label>
            <input
              type="text"
              id="tuesday"
              className="form-control"
              onChange={(e) => handleMealChange('Tuesday', e)}
              placeholder="e.g., Breakfast, Lunch, Dinner"
            />
          </div>
          <button type="submit" className="btn btn-success mt-3">
            Create Meal Plan
          </button>
        </form>
      </div>
    </div>
  );
};

export default MealPlanForm;
