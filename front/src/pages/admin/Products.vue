<script setup lang="ts">
import { ref, onMounted } from 'vue';
import PageTitle from '../../components/PageTitle.vue';
import EditIcon from '../../components/EditIcon.vue';
import DeleteIcon from '../../components/DeleteIcon.vue';
import { api } from '../../api';
import { formatCurrency } from '../../utils/currency';

const formDataInitialValues = {
  id: '',
  name: '',
  description: '',
  price: 0,
  stock_quantity: 0,
  category_id: ''
} as const;

const products = ref<any[]>([]);
const categories = ref<any[]>([]);
const isModalOpen = ref<boolean>(false);
const formData = ref<any>(formDataInitialValues);
const imageInput = ref<HTMLInputElement | null>(null);

onMounted(async () => {
  await getAllProducts();
  await getAllCategories();
});

async function getAllProducts() {
  try {
    const response = await api.get('products');
    products.value = response.data;
  } catch (error) {
    alert('Houve um erro ao carregar os produtos.');
  }
}

async function getAllCategories() {
  try {
    const response = await api.get('categories');
    categories.value = response.data;
  } catch (error) {
    alert('Houve um erro ao carregar os produtos.');
  }
}

async function handleOnClickDelete(productId: string) {
  try {
    if (!confirm('Deseja realmente excluir o produto?')) return;

    await api.delete(`products/${productId}`);
    alert('Produto excluido com sucesso!');
    await getAllProducts();
  } catch (error) {
    alert('Houve um erro ao deleter o produto');
  }
}

async function submitForm() {
  const submitData = new FormData();

  submitData.append('name', formData.value.name);
  submitData.append('description', formData.value.description);
  submitData.append('price', formData.value.price);
  submitData.append('stock_quantity', formData.value.stock_quantity);
  submitData.append('category_id', formData.value.category_id);

  if (imageInput.value?.files?.length) {
    const file = imageInput.value.files[0];
    submitData.append('image', file);
  }

  try {
    if (formData.value.id) {
      await api.put(`products/${formData.value.id}`, submitData);
      alert('Produto editado com sucesso!');
    } else {
      await api.post('products', submitData);
      alert('Produto adicionado com sucesso!');
    }
    getAllProducts();
    isModalOpen.value = false;
  } catch (error) {
    alert('Erro ao realizar requisição.');
  }
}

async function handleOnClickAddProduct() {
  resetForm();
  isModalOpen.value = true;
}

async function handleOnClickEdit(product: any) {
  formData.value.id = product.id;
  formData.value.name = product.name;
  formData.value.description = product.description;
  formData.value.price = product.price;
  formData.value.stock_quantity = product.stockQuantity;
  formData.value.category_id = product.category;
  isModalOpen.value = true;
}

function handleOnClickCancel() {
  isModalOpen.value = false;
  resetForm();
}

function resetForm() {
  formData.value.id = '';
  formData.value.name = '';
  formData.value.description = '';
  formData.value.price = 0;
  formData.value.stock_quantity = 0;
  formData.value.category_id = '';
  imageInput.value = null;
}
</script>

<template>
  <div class="grow p-5">
    <div class="flex justify-between mb-4">
      <PageTitle>Produtos</PageTitle>
      <button
        @click="handleOnClickAddProduct"
        class="px-4 bg-slate-200 hover:bg-slate-300 rounded-md"
      >
        Adicionar produto
      </button>
    </div>
    <div class="flex flex-col">
      <div
        class="grid grid-cols-5 rounded-tr-md rounded-tl-md bg-slate-600 text-white p-3"
      >
        <div>Nome</div>
        <div>Estoque</div>
        <div>Preço</div>
        <div>Data de criação</div>
        <div></div>
      </div>
      <template v-for="product in products">
        <div
          class="grid grid-cols-5 p-3 bg-slate-200 last:rounded-br-md last:rounded-bl-md"
        >
          <div>{{ product.name }}</div>
          <div>{{ product.stockQuantity }}</div>
          <div>{{ formatCurrency(product.price) }}</div>
          <div>{{ product.createdAt }}</div>
          <div class="flex justify-center gap-4">
            <button @click="() => handleOnClickEdit(product)">
              <EditIcon />
            </button>
            <button @click="() => handleOnClickDelete(product.id)">
              <DeleteIcon />
            </button>
          </div>
        </div>
      </template>
    </div>
  </div>
  <template v-if="isModalOpen">
    <div
      class="absolute h-screen w-screen top-0 left-0 bg-black bg-opacity-40 flex justify-center items-center"
    >
      <form
        class="w-1/2 bg-white rounded-md p-4 flex flex-col gap-4"
        @submit.prevent="submitForm"
      >
        <label class="flex flex-col">
          Nome do produto<input
            type="text"
            v-model="formData.name"
            placeholder="Nome"
            class="py-2 px-4 border-2 border-slate-400 rounded-md"
            required
        /></label>

        <label class="flex flex-col">
          Descrição do produto
          <input
            type="text"
            v-model="formData.description"
            placeholder="Descrição"
            class="py-2 px-4 border-2 border-slate-400 rounded-md"
            required
        /></label>

        <label class="flex flex-col"
          >Preço
          <input
            type="number"
            v-model="formData.price"
            placeholder="Preço"
            step="0.01"
            class="py-2 px-4 border-2 border-slate-400 rounded-md"
            required
        /></label>

        <label class="flex flex-col"
          >Estoque
          <input
            type="number"
            v-model="formData.stock_quantity"
            placeholder="Estoque"
            class="py-2 px-4 border-2 border-slate-400 rounded-md"
            required
        /></label>

        <label class="flex flex-col"
          >Categorias
          <select
            v-model="formData.category_id"
            class="py-2 px-4 border-2 border-slate-400 rounded-md"
            required
          >
            <template v-for="category in categories">
              <option :value="category.id">{{ category.name }}</option>
            </template>
          </select>
        </label>

        <label class="flex flex-col"
          >Imagem do Produto<input
            type="file"
            ref="imageInput"
            class="block w-full text-sm text-slate-500 file:mr-4 file:py-2 file:px-4 file:rounded-full file:border-0 file:text-sm file:font-semibold file:bg-slate-300 file:text-slate-700 hover:file:bg-slate-500 hover:file:text-white pointer"
            :required="!formData.category_id"
            accept=".png, .jpg, .jpeg"
        /></label>

        <div class="flex justify-end gap-2">
          <button
            type="submit"
            class="bg-green-300 hover:bg-green-400 rounded-md py-2 px-4"
          >
            Enviar
          </button>
          <button
            @click="handleOnClickCancel"
            class="bg-red-300 hover:bg-red-400 rounded-md py-2 px-4"
          >
            Cancelar
          </button>
        </div>
      </form>
    </div>
  </template>
</template>
