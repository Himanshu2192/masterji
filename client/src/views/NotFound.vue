<template>
  <div class="page">
    <h1>404 — Page Not Found</h1>
    <p class="lead">
      Sorry, we couldn't find the page you were looking for. It may have been moved or no longer exists.
    </p>
    <router-link to="/" class="btn">Back to Home</router-link>

    <div style="margin-top: 32px;">
      <h2 style="font-size: 1.1rem;">You might be looking for:</h2>
      <ul>
        <li><router-link to="/tour-and-travel">Tour &amp; Travel Bookings</router-link></li>
        <li><router-link to="/solar-panel-installation">Solar Panel Installation</router-link></li>
        <li><router-link to="/interior-design">Interior Design</router-link></li>
        <li><router-link to="/touring-services">Touring Services</router-link></li>
        <li><router-link to="/contact">Contact Us</router-link></li>
      </ul>
    </div>
  </div>
</template>

<script setup>
import { usePageSeo } from "../composables/usePageSeo";

// route.meta.noindex is already set to true for this route,
// so usePageSeo automatically adds <meta name="robots" content="noindex, nofollow">.
usePageSeo();
</script>
