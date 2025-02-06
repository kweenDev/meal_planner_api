/**
 * Register.js
 * Author: Refiloe Radebe
 * Date: 2025-02-06
 * Description: Component that renders the user registration form.
 */

import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import API from '../../services/api';

/**
 * Register component that handles new user registration.
 * @returns {JSX.Element} The registration form.
 */
const Register = () => {
  const [username, setUsername] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [message, setMessage] = useState('');
  const navigate = useNavigate();

  /**
   * Handles form submission for registration.
   * @param {Object} e - The form submission event.
   */
  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await API.post('/auth/register', { username, email, password });
      // Display success message and navigate to login page after registration.
      setMessage(response.data.message);
      navigate('/');
    } catch (error) {
      setMessage(error.response?.data?.message || 'Registration failed');
    }
  };

  return (
    <div className="card mx-auto" style={{ maxWidth: '400px' }}>
      <div className="card-body">
        <h2 className="card-title text-center">Register</h2>
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
            <label htmlFor="email">Email</label>
            <input
              type="email"
              id="email"
              className="form-control"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
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
            Register
          </button>
        </form>
      </div>
    </div>
  );
};

export default Register;
