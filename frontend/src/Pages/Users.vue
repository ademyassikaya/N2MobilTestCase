<template>
  <Content>
    <div class="flex flex-col">
      <h1 class="font-bold text-xl mb-9">All Users</h1>
      <div class="grid sm:grid-cols-1 lg:grid-cols-3 gap-6">
        <Card
          v-for="user in users"
          :key="user.id"
          :userId="user.id"
          :full-name="user.name"
          :email="user.email"
          :cardPhoto="getRandomImage()"
          :phone-number="user.phone"
          :informations="[
            {
              titleType: 'Location',
              titleIcon: '/location-icon.svg',
              address: user.address.street + '/' + user.address.city,
            },
            {
              titleType: 'Company',
              titleIcon: '/company-icon.svg',
              address: user.company.name,
            },
            {
              titleType: 'Website',
              titleIcon: '/website-icon.svg',
              address: user.website,
            },
          ]"
        />
      </div>
    </div>
  </Content>
</template>

<script>
import Content from "../components/Content.vue";
import ApiService from "../Services/Apiservice.js";
import Card from "../components/Card.vue";
import { ref, onMounted } from "vue";

export default {
  components: {
    Card,
    Content,
  },

  setup() {
    const users = ref([]);

    const getRandomImage = () => {
      const images = ["/userpage1.png", "/userpage2.png", "/userpage3.png"];
      const randomIndex = Math.floor(Math.random() * images.length);
      return images[randomIndex];
    };

    const getUsers = () => {
      ApiService.get("/api/users/")
        .then((response) => {
          users.value = response.data;
        })
        .catch((error) => {
          console.error("Error fetching users:", error);
        });
    };

    onMounted(getUsers);

    return {
      users,
      getRandomImage,
    };
  },
};
</script>
