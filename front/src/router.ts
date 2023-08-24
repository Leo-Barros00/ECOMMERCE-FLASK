import { RouteRecordRaw, createRouter, createWebHistory } from 'vue-router';
import DefaultLayout from './layouts/DefaultLayout.vue';
import AdminLayout from './layouts/AdminLayout.vue';

import Home from './pages/Home.vue';

const routes: RouteRecordRaw[] = [
  {
    path: '/',
    component: DefaultLayout,
    children: [
      {
        path: '',
        component: Home
      }
    ]
  },
  {
    path: '/admin',
    component: AdminLayout,
    children: [
      {
        path: '',
        component: Home
      }
    ]
  }
];

export const router = createRouter({
  history: createWebHistory(),
  routes
});
