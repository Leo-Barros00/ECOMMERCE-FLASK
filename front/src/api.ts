import axios from 'axios';

export const HOST = 'http://127.0.0.1';
export const PORT = 8000;

const api = axios.create({
  baseURL: `${HOST}:${PORT}`
});

export { api };
