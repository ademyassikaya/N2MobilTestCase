import { defineStore } from "pinia";

export const useUserStore = defineStore({
  id: "user",
  state: () => ({
    userDetails: null,
  }),
  actions: {
    setUserDetails(details) {
      this.userDetails = details;
    },
  },
});
