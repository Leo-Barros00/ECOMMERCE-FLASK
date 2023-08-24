<script setup lang="ts">
import Header from '../components/Header.vue';
import Minicart from '../components/Minicart.vue';
</script>

<template>
  <div>
    <Header />
    <Minicart />
    <router-view></router-view>
  </div>
</template>
