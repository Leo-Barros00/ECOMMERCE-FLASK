<script setup lang="ts">
import { minicart } from '../store';
import { onMounted, ref } from 'vue';
import { useRoute } from 'vue-router';
import { HOST, PORT, api } from '../api';
import PageTitle from '../components/PageTitle.vue';
import { formatCurrency } from '../utils/currency';

const product = ref<any>();

onMounted(async () => {
  const { path } = useRoute();
  const productId = path.substring(path.lastIndexOf('/') + 1);

  const { data: productParsed } = await api.get(`products/${productId}`);

  product.value = productParsed;
});

function getMinicartProductQuantity() {
  const currentProduct = minicart.products.find(
    ({ id }) => product.value.id === id
  );

  return currentProduct ? currentProduct.quantity : 0;
}

function handleOnClickAddToCart() {
  minicart.addProduct(product.value);
}
</script>

<template>
  <div class="max-w-container w-container mx-auto my-6">
    <PageTitle>Produto</PageTitle>
    <div class="mt-6 grid grid-cols-2 gap-8" v-if="product">
      <div>
        <img class="w-full" :src="`${HOST}:${PORT}${product.imageUrl}`" />
      </div>
      <div class="flex flex-col">
        <span class="text-3xl font-medium">{{ product.name }}</span>
        <span class="text-xl">{{ product.description }}</span>
        <span class="text-4xl mt-5 font-bold">{{
          formatCurrency(product.price)
        }}</span>
        <span class="mt-5 text-sm" v-if="product.stockQuantity > 0">
          Apenas {{ product.stockQuantity }} disponíveis
        </span>

        <button
          class="bg-primary text-white font-bold rounded-md py-2 px-4 mt-10 disabled:bg-gray-500 disabled:hover:ring-0 hover:ring-4 ring-red-300"
          :disabled="
            product.stockQuantity <= 0 ||
            getMinicartProductQuantity() >= product.stockQuantity
          "
          @click="handleOnClickAddToCart"
        >
          {{
            product.stockQuantity <= 0 ||
            getMinicartProductQuantity() >= product.stockQuantity
              ? 'Produto indisponível'
              : 'Adicionar ao carrinho'
          }}
        </button>
      </div>
    </div>
  </div>
</template>
