<template>
  <div class="mt-11 ml-7">
    <button
      @click="goHome"
      class="flex items-center space-x-2 px-4 py-2 font-semibold text-title rounded"
    >
      <img src="/go-home.svg" class="w-6 h-6 mr-2" alt="Go Home" />
      <span>Go Home</span>
    </button>
  </div>
</template>

<script setup>
import { useRouter } from "vue-router";

const router = useRouter();

const goHome = () => {
  router.push({ name: "users" });
};
</script>

<style scoped>
button {
  padding: 10px 20px;
  font-size: 16px;
  cursor: pointer;
}
#goHome {
  margin-left: 25px;
}
</style>
