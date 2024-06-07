<template>
  <div class="w-full h-screen overflow-y-scroll">
    <GoHome />
    <div
      v-for="(albumGroup, index) in chunkedAlbums"
      :key="index"
      class="flex justify-between mb-4 mt-3 ml-12 mr-4"
    >
      <div
        v-for="album in albumGroup"
        :key="album.id"
        @click="AlbumDetail(album.id)"
        class="w-1/3 px-4 border border-gray-300 rounded-lg mr-3 transition duration-300 ease-in-out transform hover:-translate-y-1 hover:shadow-lg"
      >
        <div class="mb-3 grid grid-cols-2 gap-0 mt-4">
          <img
            v-for="(photo, photoIndex) in albumPhotos[album.albumId]?.slice(
              0,
              4
            )"
            :src="photo?.thumbnailUrl"
            :key="photo.id"
            class="w-full h-24 object-cover aspect-w-1 aspect-h-1"
          />
        </div>
        <div class="flex font-normal font-roboto font text-center">
          {{ truncateTitle(album.title) }}
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, onMounted } from "vue";
import ApiService from "../Services/Apiservice.js";
import { useUserStore } from "../Stores/UserDetail.js";
import GoHome from "../components/GoHome.vue";
import { useRouter } from "vue-router";

export default {
  components: {
    GoHome,
  },
  setup() {
    const userStore = useUserStore();
    const albums = ref([]);
    const albumPhotos = ref({});
    const chunkedAlbums = ref([]);

    const getAlbums = () => {
      ApiService.get("/api/albums/")
        .then((response) => {
          albums.value = response.data.filter(
            (album) => album.userId == userStore.userDetails.userId
          );
          chunkedAlbums.value = chunkArray(albums.value, 3);
        })
        .catch((error) => {
          console.error("Error fetching albums:", error);
        });
    };

    const getPhotos = () => {
      ApiService.get("/api/photos/")
        .then((response) => {
          response.data.forEach((photo) => {
            if (!albumPhotos.value[photo.album]) {
              albumPhotos.value[photo.album] = [];
            }
            albumPhotos.value[photo.album].push(photo);
          });
        })
        .catch((error) => {
          console.error("Error fetching photos:", error);
        });
    };

    const chunkArray = (arr, size) => {
      const chunkedArr = [];
      for (let i = 0; i < arr.length; i += size) {
        chunkedArr.push(arr.slice(i, i + size));
      }
      return chunkedArr;
    };

    const truncateTitle = (title) => {
      const words = title.split(" ");
      if (words.length > 6) {
        return words.slice(0, 4).join(" ") + " ...";
      } else {
        return title;
      }
    };
    const router = useRouter();
    const AlbumDetail = (albumId) => {
      router.push({ name: "albumDetail", params: { albumId: albumId } });
    };

    onMounted(() => {
      getAlbums();
      getPhotos();
    });

    return { chunkedAlbums, albumPhotos, truncateTitle, AlbumDetail };
  },
};
</script>

<style scoped></style>
