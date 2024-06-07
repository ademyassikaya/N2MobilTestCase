<template>
  <div
    v-if="isOpen"
    class="fixed inset-0 flex items-center justify-center"
    style="background-color: rgba(0, 0, 0, 0.5); z-index: 9999"
    @click="closeModal"
  >
    <div
      class="relative bg-white shadow-lg rounded-xl"
      :style="modalStyle"
      @click.stop
    >
      <div class="flex justify-between items-center px-8 py-4">
        <div class="font-semibold text-title font-sans">Post Title</div>
        <div class="cursor-pointer" @click.stop="closeModal">
          <img src="/x.svg" />
        </div>
      </div>
      <div class="flex">
        <div class="overflow-y-scroll mr-1 w-7/12">
          <div class="flex font-sans text-title h-[483px] ml-8">
            {{ postData }}
          </div>
        </div>
        <div class="w-1 border-l-2"></div>
        <div
          class="flex-1 p-4 overflow-y-scroll w-5/12"
          :style="rightTextStyle"
        >
          <div class="font-sans text-title font-semibold">Comments</div>
          <div v-for="comment in comments" :key="comment.name">
            <CommentsCard :name="comment.name" :body="comment.body" />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { defineProps, defineEmits, ref, computed } from "vue";
import CommentsCard from "./CommentsCard.vue";

const props = defineProps({
  isOpen: Boolean,
  comments: Array,
  postData: String,
});

const emit = defineEmits(["modal-close"]);

const modalStyle = computed(() => ({
  width: "1024px",
  height: "609px",
  margin: "auto",
  padding: "36px 32px",
  gap: "10px",
  borderRadius: "24px",
}));

const rightTextStyle = computed(() => ({
  height: "483px",
  left: "532px",
  padding: "0px 24px 32px 24px",
  gap: "20px",
}));

const closeModal = () => {
  emit("modal-close");
};
</script>

<style scoped></style>
