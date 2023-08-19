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
    class="fixed left-full top-0 h-full z-10 duration-100 bg-slate-50 p-4"
    :class="{ '-translate-x-full': minicart.isOpen }"
  >
    aa
  </div>
</template>
