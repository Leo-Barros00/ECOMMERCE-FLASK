<script setup lang="ts">
import { ref } from 'vue';
import { HOST, PORT, api } from '../api';
import { minicart } from '../store';
import CloseIcon from './CloseIcon.vue';
import DeleteIcon from './DeleteIcon.vue';

function handleOnClickDeleteIcon(productId: string) {
  minicart.removeProduct(productId);
}

const formDataInitialValues = {
  email: '',
  address: ''
} as const;

const formData = ref<any>(formDataInitialValues);

async function submitForm() {
  await api
    .post(`products/order`, {
      status: 'pending',
      address: formData.value.address,
      email: formData.value.email,
      products: minicart.products.map(({ id, quantity }) => ({
        id,
        quantity
      }))
    })
    .then(() => {
      alert('Pedido realizado com sucesso.');
      window.location.reload();
    })
    .catch(() => {
      alert('Houve um problema ao realizar o seu pedido.');
    });
}
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
    class="fixed left-full top-0 h-full z-10 duration-100 bg-slate-50 p-6 w-full sm:w-96 flex flex-col"
    :class="{ '-translate-x-full': minicart.isOpen }"
  >
    <div class="flex justify-between items-center mb-4">
      <span class="text-2xl font-semibold">Carrinho</span>
      <button class="hover:scale-125 duration-100" @click="minicart.toggleOpen">
        <CloseIcon class="w-9 h-9 p-2" />
      </button>
    </div>
    <div class="flex flex-col grow">
      <div class="grow">
        <template v-for="product in minicart.products">
          <div class="grid grid-cols-6 gap-2">
            <div>
              <img class="w-full" :src="`${HOST}:${PORT}${product.imageUrl}`" />
            </div>
            <div class="col-span-4 flex items-center justify-between">
              <div>
                {{ product.name }}
              </div>
              <div>{{ product.quantity }}x</div>
            </div>
            <div class="flex items-center">
              <button @click="() => handleOnClickDeleteIcon(product.id)">
                <DeleteIcon />
              </button>
            </div>
          </div>
        </template>
      </div>

      <form class="flex flex-col gap-3" @submit.prevent="submitForm">
        <label class="flex flex-col">
          E-mail<input
            type="email"
            placeholder="usuario@email.com"
            v-model="formData.email"
            class="py-2 px-4 border-2 border-slate-400 rounded-md"
            required
        /></label>

        <label class="flex flex-col">
          Endereço<input
            type="mail"
            placeholder="Av. João Luiz, 325"
            v-model="formData.address"
            class="py-2 px-4 border-2 border-slate-400 rounded-md"
            required
        /></label>
        <button
          class="bg-primary text-white font-bold rounded-md py-2 px-4 hover:ring-4 ring-red-300"
          type="submit"
        >
          Finalizar pedido
        </button>
      </form>
    </div>
  </div>
</template>
