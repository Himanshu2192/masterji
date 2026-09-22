<script setup>
import { usePageSeo } from "../composables/usePageSeo";
import { SITE_NAME, SITE_URL } from "../seo";
usePageSeo({ title: `Schedule a Scrap Pickup | ${SITE_NAME}`, description: "Request a doorstep scrap pickup in Delhi-NCR.", schema: { "@context": "https://schema.org", "@type": "ContactPage", name: "Schedule a Scrap Pickup", url: `${SITE_URL}/scrap-selling/schedule` } });
</script>

<template>
  <div class="page schedule-page">
    <p class="eyebrow">Doorstep collection</p><h1>Schedule a Scrap Pickup</h1>
    <p class="lead">Tell us what you want to sell and where you are located. We will contact you to confirm the material, estimate, and pickup time.</p>
    <div class="schedule-layout">
      <div class="card schedule-card"><h2>Before you submit</h2><ul><li>Keep a rough list of materials ready.</li><li>Share approximate quantity or photos if possible.</li><li>Mention your preferred date and time.</li><li>Pickup availability is subject to Delhi-NCR location and crew schedules.</li></ul><p><strong>Prefer to talk?</strong><br /><a href="tel:+919560806929">+91 95608 06929</a></p></div>
      <div class="card"><h2>Request collection</h2><p>Use our contact form and select <strong>Scrap Selling</strong>. Include “Pickup request” in your message.</p><router-link to="/contact" class="btn">Open Pickup Form</router-link></div>
    </div>
  </div>
</template>
