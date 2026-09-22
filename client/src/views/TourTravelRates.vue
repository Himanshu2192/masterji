<script setup>
import { usePageSeo } from "../composables/usePageSeo";
import { SITE_NAME, SITE_URL } from "../seo";
const rates = [
  ["9-Seater Traveller", "₹20/km", "₹500/day"],
  ["12-Seater Traveller", "₹22/km", "₹500/day"],
  ["16-Seater Traveller", "₹22/km", "₹500/day"],
  ["18-Seater Traveller", "₹23/km", "₹500/day"],
  ["20-Seater Traveller", "₹24/km", "₹500/day"],
  ["26-Seater Traveller", "₹24/km", "₹500/day"]
];
usePageSeo({ title: `Tempo Traveller Fleet & Rates | ${SITE_NAME}`, description: "Indicative tempo traveller rental rates, capacities, driver charges, and quote conditions.", schema: { "@context": "https://schema.org", "@type": "WebPage", name: "Tempo Traveller Fleet and Rates", url: `${SITE_URL}/tour-and-travel/rates` } });
</script>
<template>
  <div class="page travel-rates-page"><p class="eyebrow">Fleet and pricing guide</p><h1>Tempo Traveller Rates</h1><p class="lead">Indicative starting rates for chauffeur-driven group travel. The final quote depends on the route, dates, vehicle availability, minimum daily kilometres, and applicable charges.</p>
    <div class="travel-rate-table"><div class="travel-rate-row travel-rate-head"><strong>Vehicle</strong><strong>Starting rate</strong><strong>Driver charge</strong></div><div v-for="rate in rates" :key="rate[0]" class="travel-rate-row"><span>{{ rate[0] }}</span><strong>{{ rate[1] }}</strong><span>{{ rate[2] }}</span></div></div>
    <div class="travel-rates-notes card"><h2>Quote conditions</h2><ul><li>Outstation plans may use a minimum of 250 km per day.</li><li>Toll, parking, state tax, government taxes, and other route charges may be extra.</li><li>Rates can change by season, route, fuel costs, and vehicle availability.</li><li>Booking is confirmed after availability and advance-payment terms are agreed.</li></ul></div>
    <router-link to="/contact" class="btn">Get a Custom Quote</router-link>
  </div>
</template>
