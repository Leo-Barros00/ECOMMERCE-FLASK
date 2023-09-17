<script setup lang="ts">
const navLinks = [
  {
    label: 'Produtos',
    href: 'products'
  },
  {
    label: 'Categorias',
    href: 'categories'
  },
  {
    label: 'Pedidos',
    href: 'orders'
  }
];
</script>

<template>
  <nav class="h-full bg-slate-50 flex flex-col gap-3 w-96 p-4">
    <template v-for="link in navLinks">
      <router-link
        :to="`/admin/${link.href}`"
        class="p-3 bg-slate-200 hover:bg-slate-300 rounded-lg inline-block"
        ><span class="text-lg font-medium">
          <span>{{ link.label }}</span>
        </span>
      </router-link>
    </template>
  </nav>
</template>
