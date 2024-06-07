<template>
  <div class="w-full h-screen overflow-y-scroll">
    <GoHome />
    <div class="ml-16 mt-20 text-gray2 font-roboto">
      <div v-for="todo in todos" :key="todo.id" class="w-[750px] h-[48px]">
        <input
          type="checkbox"
          :checked="todo.completed"
          @change="toggleComplete(todo)"
          class="w-[16px] h-[16px] border-primary text-primary focus:ring-primary checked:bg-primary checked:border-primary"
        />
        <span class="ml-3">{{ todo.title }}</span>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import { useUserStore } from "../Stores/UserDetail.js";
import GoHome from "../components/GoHome.vue";
import ApiService from "../Services/Apiservice.js";

const todos = ref([]);

const userStore = useUserStore();

const getTodos = () => {
  ApiService.get("/api/todos")
    .then((response) => {
      todos.value = response.data.filter(
        (todo) => todo.user === userStore.userDetails.userId
      );
    })
    .catch((error) => {
      console.error("Error fetching todos:", error);
    });
};

const toggleComplete = (todo) => {
  const completedStatus = !todo.completed;
  ApiService.patch(`/api/todos/${todo.id}/`, {
    completed: completedStatus,
  })
    .then(() => {
      todo.completed = completedStatus;
    })
    .catch((error) => {
      console.error("Error updating todo:", error);
    });
};

onMounted(getTodos);
</script>
