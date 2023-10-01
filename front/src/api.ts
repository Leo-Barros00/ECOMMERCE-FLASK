import axios, { AxiosResponse, AxiosError } from 'axios';

// interface RequisitionError {
//   status?: number
//   message: string
// }

const HOST = 'http://127.0.0.1';
const PORT = 5000;

const api = axios.create({
  baseURL: `${HOST}:${PORT}`
});

export { api };
