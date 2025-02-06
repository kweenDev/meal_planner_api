/**
 * NotFound.js
 * Author: Refiloe Radebe
 * Date: 2025-02-06
 * Description: Component displayed when no matching route is found.
 */

import React from 'react';

/**
 * NotFound component for unmatched routes.
 * @returns {JSX.Element} A message indicating a 404 error.
 */
const NotFound = () => (
  <div className="text-center">
    <h2>404 - Page Not Found</h2>
    <p>The page you are looking for does not exist.</p>
  </div>
);

export default NotFound;
