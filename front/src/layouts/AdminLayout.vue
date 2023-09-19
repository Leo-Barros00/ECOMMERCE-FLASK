<script setup lang="ts">
import AdminNav from '../components/AdminNav.vue';
</script>

<template>
  <div class="flex h-full">
    <AdminNav />
    <router-view></router-view>
  </div>
</template>
