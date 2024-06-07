<script setup>
import Sidebar from "./components/Sidebar.vue";
import { RouterView } from "vue-router";
import router from "./Routes.js";
</script>

<template>
  <div className="flex">
    <Sidebar />
    <RouterView />
  </div>
</template>

<style scoped></style>
