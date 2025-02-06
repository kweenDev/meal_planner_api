/**
 * MealPlanDashboard.js
 * Author: Refiloe Radebe
 * Date: 2025-02-06
 * Description: Component that displays the authenticated user's meal plans.
 */

import React, { useEffect, useState } from 'react';
import API from '../../services/api';
import MealPlanForm from './MealPlanForm';

/**
 * MealPlanDashboard component fetches and displays meal plans.
 * @returns {JSX.Element} The dashboard view.
 */
const MealPlanDashboard = () => {
  const [mealPlans, setMealPlans] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  /**
   * Fetches meal plans from the API.
   */
  const fetchMealPlans = async () => {
    try {
      const response = await API.get('/meal-planner/mealplan');
      setMealPlans(response.data.mealPlans);
    } catch (err) {
      setError('Error fetching meal plans');
    } finally {
      setLoading(false);
    }
  };

  // Refresh meal plans on component mount and when a new plan is created
  useEffect(() => {
    fetchMealPlans();
  }, []);

  if (loading) return <div>Loading meal plans...</div>;
  if (error) return <div className="alert alert-danger">{error}</div>;

  return (
    <div>
      <h2>My Meal Plans</h2>
      <MealPlanForm onSuccess={fetchMealPlans} />
      {mealPlans.length === 0 ? (
        <p>No meal plans available. Please create one.</p>
      ) : (
        <div className="list-group">
          {mealPlans.map((plan) => (
            <div key={plan.id} className="list-group-item">
              <h5>Week Starting: {plan.weekStart}</h5>
              <pre>{JSON.stringify(plan.meals, null, 2)}</pre>
            </div>
          ))}
        </div>
      )}
    </div>
  );
};

export default MealPlanDashboard;
