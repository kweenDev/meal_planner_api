/**
 * App.js
 * Author: Refiloe Radebe
 * Date: 2025-02-06
 * Description: Main application component that sets up routing and layout.
 */

import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Navbar from './components/Layout/Navbar';
import Login from './components/Auth/Login';
import Register from './components/Auth/Register';
import MealPlanDashboard from './components/MealPlan/MealPlanDashboard';
import PrivateRoute from './components/PrivateRoute';
import NotFound from './pages/NotFound';

/**
 * App component sets up the application routing.
 * @returns {JSX.Element} The main app component.
 */
const App = () => {
  return (
    <Router>
      <Navbar />
      <div className="container mt-4">
        <Routes>
          <Route path="/" element={<Login />} />
          <Route path="/register" element={<Register />} />
          <Route
            path="/meal-plans"
            element={
              <PrivateRoute>
                <MealPlanDashboard />
              </PrivateRoute>
            }
          />
          <Route path="*" element={<NotFound />} />
        </Routes>
      </div>
    </Router>
  );
};

export default App;
