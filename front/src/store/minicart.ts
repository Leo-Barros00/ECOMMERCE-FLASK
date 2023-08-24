import { reactive } from 'vue';

export default reactive({
  isOpen: false,
  toggleOpen() {
    this.isOpen = !this.isOpen;
  }
});
