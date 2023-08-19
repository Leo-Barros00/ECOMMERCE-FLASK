<script setup lang="ts">
import { minicart } from '../store';
</script>

<template>
  <header class="flex flex-col">
    <div
      class="flex justify-between items-center py-5 bg-white max-w-container w-container mx-auto"
    >
      <span class="font-bold">FlasKommerce</span>
      <button
        class="p-2 hover:scale-125 duration-100"
        @click="minicart.toggleOpen"
      >
        <img src="../assets/basket.svg" alt="Carrinho" />
      </button>
    </div>
    <div class="flex py-2 bg-emerald-300">
      <div class="max-w-container w-container mx-auto">categories</div>
    </div>
  </header>
</template>
