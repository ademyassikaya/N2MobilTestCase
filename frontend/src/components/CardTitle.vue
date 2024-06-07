<template>
  <div class="flex items-center gap-4">
    <div class="rounded-full w-[100px] h-[100px]">
      <img class="rounded-full w-[100px] h-[100px]" :src="cardPhoto" />
    </div>
    <div class="flex flex-col">
      <p class="text-lg font-semibold text-title">{{ fullName }}</p>
      <p class="font-light text-sm text-subtitle">{{ email }}</p>
      <p class="font-light text-sm text-subtitle">{{ phoneNumber }}</p>
    </div>
  </div>
</template>
<script setup>
defineProps({
  fullName: String,
  email: String,
  cardPhoto: String,
  phoneNumber: String,
});
</script>

<style scoped></style>
