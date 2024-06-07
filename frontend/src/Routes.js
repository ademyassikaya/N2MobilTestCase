import { createRouter, createWebHistory } from "vue-router";
import Users from "./Pages/Users.vue";
import TodosPage from "./Pages/Todos.vue";
import PostPage from "./Pages/Post.vue";
import AlbumsPage from "./Pages/Albums.vue";
import AlbumsDetail from "./Pages/Albums/AlbumsDetail.vue";

const routes = [
  { path: "/", component: Users, name: "users" },
  { path: "/users/:id/todos", component: TodosPage, name: "todos" },
  { path: "/users/:id/posts", component: PostPage, name: "posts" },
  { path: "/users/:id/albums", component: AlbumsPage, name: "albums" },
  {
    path: "/users/:id/albums/:albumId",
    component: AlbumsDetail,
    name: "albumDetail",
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
