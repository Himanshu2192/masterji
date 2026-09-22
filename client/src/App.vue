<template>
  <div class="app-shell">
    <AppHeader />
    <Breadcrumbs />
    <main class="app-content">
      <router-view />
    </main>
    <AppFooter />
  </div>
</template>

<script setup>
import AppHeader from "./components/AppHeader.vue";
import AppFooter from "./components/AppFooter.vue";
import Breadcrumbs from "./components/Breadcrumbs.vue";
</script>
