<template>
  <section class="related-services" aria-label="Related services">
    <h2>Explore Our Other Services</h2>
    <ul>
      <li v-for="s in otherServices" :key="s.to">
        <router-link :to="s.to">{{ s.title }}</router-link>
      </li>
    </ul>
  </section>
</template>

<script setup>
import { computed } from "vue";

const props = defineProps({
  current: { type: String, required: true } // route name of the current service page
});

const allServices = [
  { name: "tour-travel", title: "Tour & Travel Bookings", to: "/tour-and-travel" },
  { name: "solar-panel", title: "Solar Panel Installation", to: "/solar-panel-installation" },
  { name: "interior-design", title: "Interior Design", to: "/interior-design" },
  { name: "touring-services", title: "Touring Services", to: "/touring-services" },
  { name: "scrap-selling", title: "Scrap Selling", to: "/scrap-selling" }
];

const otherServices = computed(() => allServices.filter((s) => s.name !== props.current));
</script>

<style scoped>
.related-services {
  margin-top: 40px;
  padding-top: 24px;
  border-top: 1px solid #e1e8ec;
}
.related-services h2 {
  font-size: 1.1rem;
  color: #0f2a3d;
}
.related-services ul {
  list-style: none;
  padding: 0;
  display: flex;
  flex-wrap: wrap;
  gap: 14px 24px;
}
.related-services a {
  color: #164a6e;
  text-decoration: none;
  font-weight: 600;
}
.related-services a:hover {
  text-decoration: underline;
}
</style>
