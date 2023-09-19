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

// api.interceptors.response.use(
//   (response: AxiosResponse) => response,
//   ({ response, message }: AxiosError) => {
//     let error: RequisitionError

//     if (!response) {
//       error = {
//         message,
//       }
//     } else {
//       error = {
//         message: (response.data as any).message,
//         status: response.status,
//       }
//     }

//     return Promise.reject(error)
//   },
// )

export { api };
