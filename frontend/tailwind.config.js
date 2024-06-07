module.exports = {
  purge: ["./index.html", "./src/**/*.{vue,js,ts,jsx,tsx}"],
  darkMode: false, // or 'media' or 'class'
  theme: {
    extend: {
      colors: {
        subtitle: "#5C6672",
        primary: "#4F359B",
        title: "#26303E",
        border: "#D8D9DD",
        gray2: "#485B69",
        sidebar: "#F5F5F5",
        graylight: "#D8D9DD",
        sidebarselected: "#FFFFFF",
      },
      fontFamily: {
        sans: ["Poppins", "sans-serif"],
        roboto: ["Roboto", "sans-serif"],
      },
    },
  },
  variants: {
    extend: {
      backgroundColor: ["checked"],
      borderColor: ["checked"],
      textColor: ["checked"],
      ringColor: ["checked"],
    },
  },
  plugins: [require("@tailwindcss/forms")],
};
