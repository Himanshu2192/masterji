<template>
  <nav v-if="crumbs.length > 1" class="breadcrumbs" aria-label="Breadcrumb">
    <ol>
      <li v-for="(crumb, i) in crumbs" :key="crumb.path">
        <router-link v-if="i < crumbs.length - 1" :to="crumb.path">{{ crumb.label }}</router-link>
        <span v-else aria-current="page">{{ crumb.label }}</span>
      </li>
    </ol>
  </nav>
</template>

<script setup>
import { computed } from "vue";
import { useRoute } from "vue-router";
import { useHead } from "@vueuse/head";
import { absoluteUrl } from "../seo";

const route = useRoute();

const crumbs = computed(() => {
  const list = [{ path: "/", label: "Home" }];
  if (route.path !== "/") {
    list.push({ path: route.path, label: route.meta.breadcrumb || route.name });
  }
  return list;
});

// Breadcrumb structured data helps search engines show a breadcrumb trail in results.
useHead(() => ({
  script:
    crumbs.value.length > 1
      ? [
          {
            type: "application/ld+json",
            children: JSON.stringify({
              "@context": "https://schema.org",
              "@type": "BreadcrumbList",
              itemListElement: crumbs.value.map((c, i) => ({
                "@type": "ListItem",
                position: i + 1,
                name: c.label,
                item: absoluteUrl(c.path)
              }))
            })
          }
        ]
      : []
}));
</script>

<style scoped>
.breadcrumbs {
  max-width: 1100px;
  margin: 0 auto;
  padding: 14px 24px 0;
  font-size: 0.85rem;
}
.breadcrumbs ol {
  display: flex;
  flex-wrap: wrap;
  list-style: none;
  margin: 0;
  padding: 0;
  gap: 6px;
}
.breadcrumbs li:not(:last-child)::after {
  content: "/";
  margin-left: 6px;
  color: #97a4ab;
}
.breadcrumbs a {
  color: #164a6e;
  text-decoration: none;
}
.breadcrumbs a:hover {
  text-decoration: underline;
}
.breadcrumbs span[aria-current="page"] {
  color: #4b5c66;
}
</style>
