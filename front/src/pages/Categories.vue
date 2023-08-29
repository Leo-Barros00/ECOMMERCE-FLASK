<script setup lang="ts">
import PageTitle from '../components/PageTitle.vue';
import Subtitle from '../components/Subtitle.vue';
import { Category } from '../types/Category';
</script>

<template>
  <div class="max-w-container w-container mx-auto my-6">
    <PageTitle>Categorias</PageTitle>

    <div class="flex mt-8">
      <div
        class="grid grid-cols-1 gap-4"
        v-if="categories && categories.length > 0"
      >
        <template v-for="category in categories" :key="index">
          <router-link :to="'/' + category.slug">
            <Subtitle>{{
              category.name + ' (' + category.productCount + ')'
            }}</Subtitle>
          </router-link>
        </template>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
export default {
  name: 'Categories',
  data() {
    return {
      categories: [] as Category[]
    };
  },
  methods: {
    async getCategories() {
      try {
        const response = await fetch('http://127.0.0.1:5000/categories', {
          method: 'GET',
          headers: {
            accept: 'application/json'
          }
        });

        if (!response.ok) {
          throw new Error('Network response was not ok');
        }

        const data = await response.json();
        this.categories = data;
      } catch (err) {
        console.log(err);
      }
    }
  },

  async created() {
    await this.getCategories();
  }
};
</script>
