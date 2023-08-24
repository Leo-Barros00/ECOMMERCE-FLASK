<script setup lang="ts">
import PageTitle from '../components/PageTitle.vue';
</script>

<template>
  <div class="max-w-container w-container mx-auto my-6">
    <PageTitle>Categorias</PageTitle>
    <h2>{{ categories }}</h2>
  </div>
</template>

<script lang="ts">
export default {
  name: 'Categories',
  data() {
    return {
      categories: []
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
