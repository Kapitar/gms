<template>
  <Sidebar />
  <router-view />
</template>

<script>
import Sidebar from "./components/SidebarComponent.vue"

export default {
  components: {
    Sidebar
  }
}
</script>