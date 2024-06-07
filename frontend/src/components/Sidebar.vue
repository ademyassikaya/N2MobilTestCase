<template>
  <div
    class="bg-sidebar h-screen flex flex-col justify-between border-r border-graylight w-64"
  >
    <router-link
      v-if="$route.name && $route.name === 'users'"
      :to="{ name: 'users' }"
      class="w-64 h-10 gap-8 mt-6 border-r border-graylight flex items-center bg-sidebarselected"
    >
      <div
        class="w-1.5 h-10 gap-0 rounded-r-lg bg-primary overflow-hidden"
      ></div>
      <div class="flex items-center gap-3 text-primary">
        <img src="/users-icon.svg" /> Users
      </div>
    </router-link>
    <div
      v-if="
        $route.name === 'posts' ||
        $route.name === 'todos' ||
        $route.name === 'albums' ||
        $route.name === 'albumDetail'
      "
      class="mt-4"
    >
      <div
        class="flex items-center justify-center border-b border-graylight w-56 h-24 gap-6 mx-auto"
      >
        <img
          :src="userStore.userDetails.cardPhoto"
          class="w-12 h-12 gap-0 rounded-[50px]"
        />
        <div class="flex flex-col">
          <p class="text-lg font-semibold text-title">
            {{ userStore.userDetails.fullName }}
          </p>
          <p class="font-light text-sm text-subtitle">
            {{ userStore.userDetails.email }}
          </p>
        </div>
      </div>
      <router-link :to="{ name: 'todos' }">
        <div
          v-if="$route.name === 'todos'"
          class="w-64 h-10 gap-8 mt-16 border-r border-graylight flex items-center bg-sidebarselected"
        >
          <div class="w-1.5 h-10 gap-0 rounded-r-lg bg-primary"></div>
          <div class="flex items-center gap-3 text-primary">
            <img src="/check-up-list.svg" /> Todos
          </div>
        </div>
        <div
          v-else
          class="w-64 h-10 gap-8 mt-16 border-r border-graylight flex items-center"
        >
          <div class="w-1.5 h-10 gap-0 rounded-r-lg bg-transparent"></div>
          <div class="flex items-center gap-3 text-primary">
            <img src="/check-up-list.svg" /> Todos
          </div>
        </div>
      </router-link>

      <router-link :to="{ name: 'posts' }">
        <div
          v-if="$route.name === 'posts'"
          class="w-64 h-10 gap-8 mt-6 border-r border-graylight flex items-center bg-sidebarselected"
        >
          <div class="w-1.5 h-10 gap-0 rounded-r-lg bg-primary"></div>
          <div class="flex items-center gap-3 text-primary">
            <img src="/note-book.svg" /> Posts
          </div>
        </div>
        <div
          v-else
          class="w-64 h-10 gap-8 mt-6 border-r border-graylight flex items-center"
        >
          <div class="w-1.5 h-10 gap-0 rounded-r-lg bg-transparent"></div>
          <div class="flex items-center gap-3 text-primary">
            <img src="/note-book.svg" /> Posts
          </div>
        </div>
      </router-link>

      <router-link :to="{ name: 'albums' }">
        <div
          v-if="$route.name === 'albums' || $route.name === 'albumDetail'"
          class="w-64 h-10 gap-8 mt-6 border-r border-graylight flex items-center bg-sidebarselected"
        >
          <div class="w-1.5 h-10 gap-0 rounded-r-lg bg-primary"></div>
          <div class="flex items-center gap-3 text-primary">
            <img src="/photo-heart.svg" /> Albums
          </div>
        </div>
        <div
          v-else
          class="w-64 h-10 gap-8 mt-6 border-r border-graylight flex items-center"
        >
          <div class="w-1.5 h-10 gap-0 rounded-r-lg bg-transparent"></div>
          <div class="flex items-center gap-3 text-primary">
            <img src="/photo-heart.svg" /> Albums
          </div>
        </div>
      </router-link>
    </div>
    <div
      class="flex items-center justify-center border-t border-graylight w-56 h-16 gap-6 mx-auto"
      @click="mainPage"
    >
      <img src="/N2MobilIcon.svg" />
      <a class="text-gray2 font-bold font-sans">N2Mobil</a>
    </div>
  </div>
</template>

<script setup>
import { useUserStore } from "../Stores/UserDetail.js";
import { useRouter } from "vue-router";
const userStore = useUserStore();
const router = useRouter();

const mainPage = () => {
  router.push({ name: "users" });
};
</script>

<style scoped></style>
