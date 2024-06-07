<template>
  <div class="w-full h-screen overflow-y-scroll">
    <GoHome />
    <div class="ml-16 mr-16">
      <LongCard
        v-for="(post, index) in posts"
        :key="index"
        :title="post.title"
        :body="post.body"
        :postId="post.id"
      />
    </div>
  </div>
</template>

<script>
import GoHome from "../components/GoHome.vue";
import LongCard from "../components/LongCard.vue";
import { ref, onMounted } from "vue";
import { useUserStore } from "../Stores/UserDetail.js";
import ApiService from "../Services/Apiservice.js";

export default {
  components: {
    GoHome,
    LongCard,
  },
  setup() {
    const userStore = useUserStore();
    const posts = ref([]);

    const getPosts = () => {
      ApiService.get("/api/posts")
        .then((response) => {
          posts.value = response.data.filter(
            (post) => post.userId === userStore.userDetails.userId
          );
        })
        .catch((error) => {
          console.error("Error fetching posts:", error);
        });
    };

    onMounted(getPosts);

    return { posts };
  },
};
</script>
