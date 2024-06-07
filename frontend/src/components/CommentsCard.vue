<template>
  <div class="flex mt-5">
    <img class="rounded-full w-[50px] h-[50px] mr-3" :src="getRandomImage()" />
    <div>
      <p class="text-lg font-semibold text-title">{{ name }}</p>
      <p class="font-light text-sm text-subtitle">{{ body }}</p>
    </div>
  </div>
</template>

<script setup>
defineProps({
  name: String,
  body: String,
});
const getRandomImage = () => {
  const images = ["/userpage1.png", "/userpage2.png", "/userpage3.png"];
  const randomIndex = Math.floor(Math.random() * images.length);
  return images[randomIndex];
};
</script>

<style scoped></style>
