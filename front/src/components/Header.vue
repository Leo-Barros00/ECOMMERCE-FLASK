<script setup lang="ts">
import { minicart } from '../store';
import BasketIcon from './BasketIcon.vue';
import MenuIcon from './MenuIcon.vue';

function getMinicartTotalItems() {
  return minicart.products.reduce((pv, { quantity }) => pv + quantity, 0);
}
</script>

<template>
  <header class="flex flex-col bg-primary">
    <div
      class="flex justify-between items-center py-5 text-white max-w-container w-container mx-auto"
    >
      <router-link to="/"
        ><span class="font-bold text-2xl">FlasKommerce</span></router-link
      >
      <button
        class="p-2 hover:scale-125 duration-100 relative"
        @click="minicart.toggleOpen"
      >
        <basket-icon class="fill-white" />
        <div
          v-if="getMinicartTotalItems() > 0"
          class="absolute bg-black aspect-square rounded-full text-xs w-4 h-4 right-0 top-0"
        >
          {{ getMinicartTotalItems() }}
        </div>
      </button>
    </div>
    <div class="flex bg-secondary text-white text-lg font-medium">
      <div
        class="max-w-container w-container mx-auto flex justify-between flex-wrap gap-x-8 relative"
      >
        <router-link to="/categories"
          ><span class="group flex gap-3 py-3 items-center">
            <menu-icon class="fill-white" />
            <span>Todas as categorias</span>
          </span></router-link
        >
      </div>
    </div>
  </header>
</template>
