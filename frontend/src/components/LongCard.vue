<template>
  <div class="relative grid grid-cols-12 border-b border-graylight">
    <div class="col-span-6 pb-[75px] px-5">
      <div class="mb-2 mt-5 font-medium font-sans text-title">{{ title }}</div>
      <div class="font-normal font-sans text-subtitle">{{ truncatedBody }}</div>
    </div>
    <div
      class="absolute flex bottom-0 right-0 pt-3 pb-5 pr-5"
      @click="postModel"
    >
      <span class="mr-4">See More</span>
      <img src="/right-arrow.svg" />
    </div>
  </div>
  <ModalComponent
    :isOpen="isModalOpen"
    :comments="comments"
    :postData="body"
    @modal-close="isModalOpen = false"
  />
</template>

<script setup>
import { ref, computed } from "vue";
import { defineProps } from "vue";
import ModalComponent from "../components/Modal.vue";
import ApiService from "../Services/Apiservice.js";

const props = defineProps({
  title: String,
  body: String,
  postId: Number,
});

const comments = ref([]);
const isModalOpen = ref(false);

const truncatedBody = computed(() => {
  const words = props.body.split(" ");
  return words.length > 30 ? words.slice(0, 30).join(" ") + "..." : props.body;
});

const postModel = () => {
  ApiService.get("/api/comments/")
    .then((response) => {
      comments.value = response.data.filter(
        (comment) => comment.post === props.postId
      );
      isModalOpen.value = true;
    })
    .catch((error) => {
      console.error("Error fetching comments:", error);
    });
};
</script>
