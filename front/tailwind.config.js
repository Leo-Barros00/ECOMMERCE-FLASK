/** @type {import('tailwindcss').Config} */
export default {
  content: ["./index.html", "./src/**/*.{vue,js,ts,jsx,tsx}"],
  theme: {
    extend: {
      width: {
        container: "92.5vw"
      },
      maxWidth: {
        container: "1280px"
      }
    }
  },
  plugins: []
};
