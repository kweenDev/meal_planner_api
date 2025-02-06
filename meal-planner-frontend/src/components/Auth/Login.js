/**
 * Login.js
 * Author: Refiloe Radebe
 * Date: 2025-02-06
 * Description: Component that renders the user login form.
 */

import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import API from '../../services/api';

/**
 * Login component that handles user login.
 * @returns {JSX.Element} The login form.
 */
const Login = () => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [message, setMessage] = useState('');
  const navigate = useNavigate();

  /**
   * Handles form submission for login.
   * Sends a POST request to the backend and upon success, stores the JWT token.
   * @param {Object} e - The form submission event.
   */
  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await API.post('/auth/login', { username, password });
      localStorage.setItem('access_token', response.data.access_token);
      setMessage('Login successful!');
      navigate('/meal-plans');
    } catch (error) {
      setMessage(error.response?.data?.message || 'Login failed');
    }
  };

  return (
    <div className="card mx-auto" style={{ maxWidth: '400px' }}>
      <div className="card-body">
        <h2 className="card-title text-center">Login</h2>
        {message && <div className="alert alert-info">{message}</div>}
        <form onSubmit={handleSubmit}>
          <div className="form-group">
            <label htmlFor="username">Username</label>
            <input
              type="text"
              id="username"
              className="form-control"
              value={username}
              onChange={(e) => setUsername(e.target.value)}
              required
            />
          </div>
          <div className="form-group mt-2">
            <label htmlFor="password">Password</label>
            <input
              type="password"
              id="password"
              className="form-control"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              required
            />
          </div>
          <button type="submit" className="btn btn-primary w-100 mt-3">
            Login
          </button>
        </form>
      </div>
    </div>
  );
};

export default Login;
