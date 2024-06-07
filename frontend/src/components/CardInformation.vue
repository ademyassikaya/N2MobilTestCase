<template>
  <div class="flex flex-col">
    <div class="flex gap-2">
      <span><img :src="titleIcon" /></span>
      <span class="text-sm font-medium text-information-title">
        {{ titleType }}
      </span>
    </div>
    <p class="text-sm text-subtitle">
      {{ address }}
    </p>
  </div>
</template>
<script setup>
defineProps({
  titleType: String,
  titleIcon: String,
  address: String,
});
</script>

<style scoped></style>
