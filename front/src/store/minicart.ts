import { reactive } from 'vue';

export default reactive({
  isOpen: false,
  toggleOpen() {
    this.isOpen = !this.isOpen;
  },
  products: [] as any[],
  address: '',
  email: '',
  addProduct(product: any) {
    console.log({ product });
    const existingProduct = this.products.find(({ id }) => id === product.id);

    if (existingProduct) {
      existingProduct.quantity += 1;
    } else {
      this.products.push({
        ...product,
        quantity: 1
      });
    }
  },
  removeProduct(productId: string) {
    this.products = this.products.filter(({ id }) => productId !== id);
  },
  removeAllProducts() {
    this.products = [];
  }
});
