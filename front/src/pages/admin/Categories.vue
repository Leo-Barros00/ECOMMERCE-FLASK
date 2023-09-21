<script setup lang="ts">
import { onMounted, ref } from 'vue';
import PageTitle from '../../components/PageTitle.vue';
import { api } from '../../api';
import EditIcon from '../../components/EditIcon.vue';
import DeleteIcon from '../../components/DeleteIcon.vue';

const formDataInitialValues = {
  id: '',
  name: ''
} as const;

const isModalOpen = ref<boolean>(false);
const formData = ref<any>(formDataInitialValues);
const categories = ref<any[]>([]);

onMounted(async () => {
  await getAllCategories();
});

async function getAllCategories() {
  try {
    const response = await api.get('categories');
    categories.value = response.data;
  } catch (error) {
    alert('Houve um erro ao carregar os produtos.');
  }
}

async function handleOnClickAddProduct() {
  resetForm();
  isModalOpen.value = true;
}

async function handleOnClickDelete({ id, productCount }: any) {
  try {
    if (productCount > 0)
      return alert(
        'Não é possível deletar essa categoria, possui produtos cadastrados.'
      );
    if (!confirm('Deseja realmente excluir a categoria?')) return;

    await api.delete(`categories/${id}`);
    alert('Categoria excluida com sucesso!');
    await getAllCategories();
  } catch (error) {
    alert('Houve um erro ao deleter a categoria.');
  }
}

async function handleOnClickEdit(category: any) {
  formData.value.id = category.id;
  formData.value.name = category.name;
  isModalOpen.value = true;
}

function resetForm() {
  formData.value.id = '';
  formData.value.name = '';
}

async function submitForm() {
  try {
    const body = {
      name: formData.value.name
    };
    if (formData.value.id) {
      await api.put(`categories/${formData.value.id}`, body);
      alert('Categoria editada com sucesso!');
    } else {
      await api.post('categories', body);
      alert('Categoria adicionada com sucesso!');
    }
    getAllCategories();
    isModalOpen.value = false;
  } catch (error) {
    alert('Erro ao realizar requisição.');
  }
}

function handleOnClickCancel() {
  isModalOpen.value = false;
  resetForm();
}
</script>

<template>
  <div class="grow p-5">
    <div class="flex justify-between mb-4">
      <PageTitle>Categorias</PageTitle>
      <button
        @click="handleOnClickAddProduct"
        class="px-4 bg-slate-200 hover:bg-slate-300 rounded-md"
      >
        Adicionar categoria
      </button>
    </div>
    <div class="flex flex-col">
      <div
        class="grid grid-cols-3 rounded-tr-md rounded-tl-md bg-slate-600 text-white p-3"
      >
        <div>Nome</div>
        <div>Número de Produtos</div>
        <div></div>
      </div>
      <template v-for="category in categories">
        <div
          class="grid grid-cols-3 p-3 bg-slate-200 last:rounded-br-md last:rounded-bl-md"
        >
          <div>{{ category.name }}</div>
          <div>{{ category.productCount }}</div>
          <div class="flex justify-center gap-4">
            <button @click="() => handleOnClickEdit(category)">
              <EditIcon />
            </button>
            <button @click="() => handleOnClickDelete(category)">
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
          Nome da categoria<input
            type="text"
            v-model="formData.name"
            placeholder="Nome"
            class="py-2 px-4 border-2 border-slate-400 rounded-md"
            required
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
