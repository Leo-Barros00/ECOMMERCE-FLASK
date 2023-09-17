import { RouteRecordRaw, createRouter, createWebHistory } from 'vue-router';
import DefaultLayout from './layouts/DefaultLayout.vue';
import AdminLayout from './layouts/AdminLayout.vue';

// Normal Pages
import Home from './pages/Home.vue';
import Categories from './pages/Categories.vue';

// Admin Pages
import Products from './pages/admin/Products.vue';

const routes: RouteRecordRaw[] = [
  {
    path: '/',
    component: DefaultLayout,
    children: [
      {
        path: '',
        component: Home
      },
      {
        path: 'categories',
        component: Categories,
        meta: { title: 'Categorias' }
      },
      {
        path: ':categorySlug',
        component: Home
      }
    ]
  },
  {
    path: '/admin',
    component: AdminLayout,
    children: [
      {
        path: 'products',
        component: Products,
        meta: { title: 'Painel administrativo - Produtos' }
      }
    ]
  }
];

export const router = createRouter({
  history: createWebHistory(),
  routes
});

router.beforeEach((to, _, next) => {
  const hasDefaultTitle = to.meta && to.meta.title;
  if (hasDefaultTitle) {
    document.title = `FlasKommerce | ${to.meta.title}`;
  } else {
    document.title = 'FlasKommerce';
  }
  next();
});
