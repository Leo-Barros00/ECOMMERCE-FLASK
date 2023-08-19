<script setup lang="ts">
import { minicart } from '../store';
</script>

<template>
  <div
    class="absolute w-full h-full left-0 top-0 bg-black duration-100"
    :class="{
      'pointer-events-none': !minicart.isOpen,
      'opacity-0': !minicart.isOpen,
      'opacity-20': minicart.isOpen
    }"
    @click="minicart.toggleOpen"
  ></div>
  <div
    class="fixed left-full top-0 h-full z-10 duration-100 bg-slate-50 p-6 w-full sm:w-96"
    :class="{ '-translate-x-full': minicart.isOpen }"
  >
    <div class="flex justify-between items-center">
      <span class="text-2xl font-semibold">Carrinho</span>
      <button class="hover:scale-125 duration-100" @click="minicart.toggleOpen">
        <img src="../assets/close.svg" alt="Fechar carrinho" class="w-9 p-2" />
      </button>
    </div>
    <div>
      <!-- CART CONTENT/BODY -->
    </div>
  </div>
</template>
