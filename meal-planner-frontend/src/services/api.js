/**
 * api.js
 * Author: Refiloe Radebe
 * Date: 2025-02-06
 * Description: Axios instance for making API requests to the backend.
 */

import axios from 'axios';

// Create an Axios instance with the base URL of the backend API
const API = axios.create({
  baseURL: ProcessingInstruction.env.REACT_APP_API_URL || 'http://localhost:5000/api/v1',
});

// Axios interceptor to attach JWT token to every request if available
API.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('access_token');
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => Promise.reject(error)
);

export default API;
