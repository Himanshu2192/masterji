<script setup>
import { usePageSeo } from "../composables/usePageSeo";
import { SITE_NAME, SITE_URL } from "../seo";

const rates = [
  { category: "Paper & cardboard", items: [["Newspaper", "₹11–13 / kg"], ["Books", "₹11–13 / kg"], ["Office paper", "₹11–13 / kg"], ["Cardboard", "₹7–8 / kg"], ["Clothes", "₹1–2 / kg"]] },
  { category: "E-waste & appliances", items: [["Laptop", "₹500 / unit"], ["Computer CPU", "₹400 / unit"], ["Single-door fridge", "₹1,100 / unit"], ["1.5-ton AC", "₹4,500 / unit"], ["2-ton AC", "₹5,600 / unit"], ["Washing machine", "₹800–1,350 / unit"], ["UPS", "₹180 / unit"]] },
  { category: "Metals & other scrap", items: [["Iron / loha", "Quote after weighing"], ["Aluminium", "Quote after weighing"], ["Copper / brass", "Quote after weighing"], ["Batteries", "Quote after inspection"], ["Gym / construction scrap", "Custom quote"]] }
];

usePageSeo({ title: `Scrap Rates | ${SITE_NAME}`, description: "Indicative scrap rates for paper, metals, e-waste, appliances, and household recyclables.", schema: { "@context": "https://schema.org", "@type": "WebPage", name: "Scrap Rates", url: `${SITE_URL}/scrap-selling/rates` } });
</script>

<template>
  <div class="page rates-page">
    <p class="eyebrow">Transparent pricing</p><h1>Indicative Scrap Rates</h1>
    <p class="lead">Use these rates as a planning guide. Final payment depends on current market rates, material condition, quantity, and verified weight at pickup.</p>
    <div class="rate-grid">
      <article v-for="group in rates" :key="group.category" class="card rate-card">
        <h2>{{ group.category }}</h2>
        <div v-for="item in group.items" :key="item[0]" class="rate-row"><span>{{ item[0] }}</span><strong>{{ item[1] }}</strong></div>
      </article>
    </div>
    <p class="rate-note">Rates can change. We confirm the applicable estimate before or at the time of collection.</p>
    <router-link to="/scrap-selling/schedule" class="btn">Schedule a Pickup</router-link>
  </div>
</template>
