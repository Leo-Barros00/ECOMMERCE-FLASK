<script setup lang="ts">
import { onMounted, ref } from 'vue';
import PageTitle from '../components/PageTitle.vue';
import { HOST, PORT, api } from '../api';
import { useRoute } from 'vue-router';
import { formatCurrency } from '../utils/currency';

const category = ref<any>();

onMounted(async () => {
  const { path } = useRoute();

  const { data: categoryParsed } = await api.get(`categories/slug/${path}`);

  category.value = categoryParsed;
});
</script>

<template>
  <div class="max-w-container w-container mx-auto my-6">
    <PageTitle v-if="category">{{ category.name }}</PageTitle>
    <div v-if="category" class="grid grid-cols-4 my-10">
      <template v-for="product in category.products">
        <router-link :to="'/' + category.slug + '/' + product.id">
          <div class="p-4 rounded-sm shadow-md">
            <img
              :src="`${HOST}:${PORT}${product.imageUrl}`"
              class="h-40 mx-auto object-contain"
            />
            <div class="flex flex-col">
              <span class="font-bold text-2xl">
                {{ product.name }}
              </span>
              <span>
                {{ formatCurrency(product.price) }}
              </span>
            </div>
          </div>
        </router-link>
      </template>
    </div>
  </div>
</template>
