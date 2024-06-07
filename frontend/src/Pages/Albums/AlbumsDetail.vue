<template>
  <div>
    <goAlbums />
    <div v-if="albumPhotos.length > 0" class="flex photo-list ml-12">
      <div
        v-for="photo in albumPhotos"
        :key="photo.id"
        class="photo-item w-1/5 mr-6"
      >
        <img :src="photo.thumbnailUrl" class="" alt="Photo" />
      </div>
    </div>
    <div v-else>
      <p class="ml-12">No photos found for this album</p>
    </div>
  </div>
</template>

<script>
import { ref, onMounted } from "vue";
import ApiService from "../../Services/Apiservice.js";
import goAlbums from "../../components/GoALbum.vue";
import { useRoute } from "vue-router";

export default {
  components: {
    goAlbums,
  },
  setup() {
    const route = useRoute();
    const albumId = route.params.albumId;
    const albumPhotos = ref([]);

    const getPhotos = () => {
      ApiService.get("/api/photos/")
        .then((response) => {
          albumPhotos.value = response.data.filter(
            (albumPhotos) => albumPhotos.albumId == albumId
          );
        })
        .catch((error) => {
          console.error("Error fetching photos:", error);
        });
    };
    onMounted(() => {
      getPhotos();
    });
    return { albumPhotos };
  },
};
</script>
