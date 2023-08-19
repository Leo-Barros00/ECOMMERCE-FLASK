import { reactive } from "vue";

export default reactive({
  isOpen: true,
  toggleOpen() {
    this.isOpen = !this.isOpen;
  }
});
