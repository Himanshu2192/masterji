<template>
  <header class="site-header">
    <div class="header-inner">
      <router-link to="/" class="brand">
        <img src="/favicon.svg" alt="Masterji Consultancy logo" width="28" height="28" />
        <span>Masterji Consultancy</span>
      </router-link>

      <button
        class="nav-toggle"
        @click="menuOpen = !menuOpen"
        :aria-expanded="menuOpen"
        aria-label="Toggle navigation menu"
      >
        <span></span><span></span><span></span>
      </button>

      <nav :class="['main-nav', { open: menuOpen }]" aria-label="Main navigation">
        <router-link to="/" @click="menuOpen = false">Home</router-link>

        <div class="dropdown">
          <span class="dropdown-label">Services ▾</span>
          <div class="dropdown-menu">
            <router-link to="/tour-and-travel" @click="menuOpen = false">Tour &amp; Travel Bookings</router-link>
            <router-link to="/solar-panel-installation" @click="menuOpen = false">Solar Panel Installation</router-link>
            <router-link to="/interior-design" @click="menuOpen = false">Interior Design</router-link>
            <router-link to="/touring-services" @click="menuOpen = false">Touring Services</router-link>
            <router-link to="/scrap-selling" @click="menuOpen = false">Scrap Selling</router-link>
          </div>
        </div>

        <router-link to="/contact" @click="menuOpen = false">Contact</router-link>
      </nav>
    </div>
  </header>
</template>

<script setup>
import { ref, watch } from "vue";
import { useRoute } from "vue-router";
const menuOpen = ref(false);
const route = useRoute();
watch(() => route.path, () => {
  menuOpen.value = false;
});
</script>

<style scoped>
.site-header {
  background: #0f2a3d;
  color: #fff;
  position: sticky;
  top: 0;
  z-index: 50;
}
.header-inner {
  max-width: 1200px;
  margin: 0 auto;
  padding: 14px 24px;
  display: flex;
  align-items: center;
  justify-content: space-between;
}
.brand {
  color: #fff;
  font-weight: 700;
  font-size: 1.25rem;
  text-decoration: none;
  letter-spacing: 0.3px;
  display: flex;
  align-items: center;
  gap: 10px;
}
.main-nav {
  display: flex;
  align-items: center;
  gap: 28px;
}
.main-nav a {
  color: #e6edf3;
  text-decoration: none;
  font-size: 0.95rem;
}
.main-nav a.router-link-exact-active {
  color: #f2a71b;
}
.dropdown {
  position: relative;
}
.dropdown-label {
  cursor: pointer;
  color: #e6edf3;
  font-size: 0.95rem;
}
.dropdown-menu {
  display: none;
  position: absolute;
  top: 100%;
  left: 0;
  background: #ffffff;
  color: #0f2a3d;
  min-width: 220px;
  border-radius: 6px;
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.18);
  padding: 8px 0;
  margin-top: 10px;
}
.dropdown:hover .dropdown-menu,
.dropdown:focus-within .dropdown-menu {
  display: block;
}
.dropdown-menu a {
  display: block;
  padding: 10px 18px;
  color: #0f2a3d;
  white-space: nowrap;
}
.dropdown-menu a:hover {
  background: #f2f6f8;
}
.nav-toggle {
  display: none;
  flex-direction: column;
  gap: 4px;
  background: none;
  border: none;
  cursor: pointer;
}
.nav-toggle span {
  width: 24px;
  height: 2px;
  background: #fff;
}

@media (max-width: 820px) {
  .nav-toggle {
    display: flex;
  }
  .main-nav {
    display: none;
    position: absolute;
    top: 100%;
    left: 0;
    right: 0;
    background: #0f2a3d;
    flex-direction: column;
    align-items: flex-start;
    padding: 16px 24px;
    gap: 14px;
  }
  .main-nav.open {
    display: flex;
  }
  .dropdown-menu {
    position: static;
    box-shadow: none;
    margin-top: 8px;
    background: #133650;
  }
  .dropdown-menu a {
    color: #e6edf3;
  }
  .dropdown-menu a:hover {
    background: #164a6e;
  }
}
</style>
