<template>
  <div
    class="flex justify-center items-center rounded-xl border border-graylight w-full hover:shadow-n2 duration-500"
    @click="
      goToTodosPage(
        userId,
        fullName,
        email,
        cardPhoto,
        informations,
        phoneNumber
      )
    "
  >
    <div class="flex flex-col gap-8 py-5 px-6">
      <CardTitle
        :fullName="fullName"
        :email="email"
        :cardPhoto="cardPhoto"
        :phoneNumber="phoneNumber"
      />

      <div class="w-[259px] flex flex-col">
        <CardInformation
          v-for="information in informations"
          :key="information.id"
          :titleType="information.titleType"
          :titleIcon="information.titleIcon"
          :address="information.address"
        />
      </div>
    </div>
  </div>
</template>

<script setup>
import CardInformation from "./CardInformation.vue";
import CardTitle from "./CardTitle.vue";
import { useUserStore } from "../Stores/UserDetail.js";
import { useRouter } from "vue-router";

const router = useRouter();
const userStore = useUserStore();

const goToTodosPage = (
  userId,
  fullName,
  email,
  cardPhoto,
  informations,
  phoneNumber
) => {
  userStore.setUserDetails({
    userId,
    fullName,
    email,
    cardPhoto,
    informations,
    phoneNumber,
  });

  router.push({ path: `/users/${userId}/todos` });
};
defineProps({
  userId: Number,
  fullName: String,
  email: String,
  cardPhoto: String,
  informations: Array,
  phoneNumber: String,
});
</script>
