/**
 * PrivateRoute.js
 * Author: Refiloe Radebe
 * Date: 2025-02-06
 * Description: Component to protect routes from unauthenticated access.
 */

import React from 'react';
import { Navigate } from 'react-router-dom';

/**
 * PrivateRoute component checks for authentication.
 * @param {Object} props - The component props.
 * @returns {JSX.Element} Either the child component or a redirect to login.
 */
const PrivateRoute = ({ children }) => {
  const isAuthenticated = Boolean(localStorage.getItem('access_token'));
  return isAuthenticated ? children : <Navigate to="/" />;
};

export default PrivateRoute;
