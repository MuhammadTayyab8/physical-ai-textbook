// /src/utils/environment.js
// Set up environment variables for the client
const API_URL = typeof process !== 'undefined' 
  ? (process.env.REACT_APP_API_URL || process.env.API_URL || 'http://127.0.0.1:8000') 
  : 'http://127.0.0.1:8000';

if (typeof window !== 'undefined') {
  window.API_CONFIG = {
    API_URL: API_URL
  };
}