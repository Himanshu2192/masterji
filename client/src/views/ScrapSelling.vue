<script setup>
import { usePageSeo } from "../composables/usePageSeo";
import { SITE_NAME, SITE_URL } from "../seo";

const recyclableCategories = [
  { icon: "📄", title: "Paper & cardboard", text: "Newspapers, books, office paper, cartons, and packaging." },
  { icon: "🔩", title: "Metals", text: "Iron, aluminium, copper, brass, batteries, and household metal." },
  { icon: "💻", title: "E-waste & IT", text: "Laptops, CPUs, TVs, printers, monitors, cables, and accessories." },
  { icon: "🧺", title: "Appliances", text: "Fridges, ACs, washing machines, geysers, UPS units, and more." },
  { icon: "♻️", title: "Plastics", text: "Sorted household, shop, and office plastic items for recycling." },
  { icon: "🏗️", title: "Other scrap", text: "Gym equipment, construction material, and larger metal items." }
];

const steps = [
  { number: "1", title: "Schedule a pickup", text: "Share your location, preferred time, and the scrap you want to sell." },
  { number: "2", title: "We collect at your doorstep", text: "Our pickup crew reviews and weighs your items using a digital scale." },
  { number: "3", title: "Get paid instantly", text: "Receive payment on the spot before the crew leaves." }
];

const householdPoints = ["Free doorstep collection", "On-demand scheduled pickups", "Accurate digital weighing", "Trained and verified pickup crew"];
const businessPoints = ["Bulk scrap collection", "Formal payments and documentation", "Competitive rates for regular volumes", "Sustainability and ESG reporting support"];

usePageSeo({
  schema: [
    {
      "@context": "https://schema.org",
      "@type": "Service",
      serviceType: "Doorstep Scrap Pickup",
      provider: { "@type": "LocalBusiness", name: SITE_NAME, url: SITE_URL },
      areaServed: "Delhi-NCR",
      description: "Schedule a doorstep scrap pickup, get your recyclables weighed digitally, and receive payment before collection is complete."
    },
    {
      "@context": "https://schema.org",
      "@type": "WebPage",
      name: "Scrap Selling and Doorstep Pickup",
      url: `${SITE_URL}/scrap-selling`
    }
  ]
});
</script>

<template>
  <div class="scrap-page">
    <section class="scrap-hero">
      <div class="scrap-hero-inner">
        <div class="scrap-hero-copy">
          <p class="eyebrow">Delhi-NCR doorstep scrap pickup</p>
          <h1>Sell your scrap online. Get paid instantly.</h1>
          <p>Schedule a pickup, we collect from your doorstep, weigh your recyclables digitally, and pay you before we leave.</p>
          <div class="scrap-actions">
            <router-link to="/scrap-selling/schedule" class="btn">Schedule a Pickup</router-link>
            <router-link to="/scrap-selling/rates" class="scrap-secondary-btn">View Indicative Rates</router-link>
          </div>
          <p class="scrap-trust-line">Simple booking · Doorstep collection · Instant payment</p>
        </div>
        <img src="https://images.unsplash.com/photo-1532996122724-e3c354a0b15b?auto=format&fit=crop&w=1200&q=85" alt="Sorted recyclable materials ready for collection" width="1200" height="800" />
      </div>
    </section>

    <section class="scrap-section scrap-container">
      <div class="scrap-section-heading">
        <p class="eyebrow">How it works</p>
        <h2>Three simple steps from scrap to payment</h2>
      </div>
      <div class="scrap-steps">
        <article v-for="step in steps" :key="step.number" class="scrap-step">
          <span>{{ step.number }}</span>
          <h3>{{ step.title }}</h3>
          <p>{{ step.text }}</p>
        </article>
      </div>
    </section>

    <section class="scrap-section scrap-container">
      <div class="scrap-section-heading">
        <p class="eyebrow">What we collect</p>
        <h2>Turn everyday recyclables into value</h2>
        <p>Not sure whether we collect something? Send us a list or photo and we will help you identify the right category.</p>
      </div>
      <div class="scrap-category-grid">
        <article v-for="category in recyclableCategories" :key="category.title" class="scrap-category">
          <span aria-hidden="true">{{ category.icon }}</span>
          <div><h3>{{ category.title }}</h3><p>{{ category.text }}</p></div>
        </article>
      </div>
      <router-link to="/scrap-selling/accepted-materials" class="text-link">See accepted materials →</router-link>
    </section>

    <section class="scrap-section scrap-container">
      <div class="scrap-audience-grid">
        <article class="scrap-audience">
          <p class="eyebrow">For households</p>
          <h2>Clear out your home without the hassle</h2>
          <ul><li v-for="point in householdPoints" :key="point">{{ point }}</li></ul>
          <router-link to="/scrap-selling/schedule" class="btn">Book Home Pickup</router-link>
        </article>
        <article class="scrap-audience business">
          <p class="eyebrow">For businesses</p>
          <h2>Make your regular scrap work harder</h2>
          <ul><li v-for="point in businessPoints" :key="point">{{ point }}</li></ul>
          <router-link to="/contact" class="btn">Discuss Bulk Collection</router-link>
        </article>
      </div>
    </section>

    <section class="scrap-section scrap-container">
      <div class="scrap-journey">
        <div>
          <p class="eyebrow">From pickup to recycling</p>
          <h2>A more responsible circular journey</h2>
          <p>Your scrap is sorted by material so recyclable items can move towards processing, reuse, and recovery instead of being left mixed with everyday waste.</p>
        </div>
        <div class="journey-points"><span>Collect</span><b>→</b><span>Sort</span><b>→</b><span>Process</span><b>→</b><span>Reuse</span></div>
      </div>
    </section>

    <section class="scrap-cta">
      <div class="scrap-container scrap-cta-inner">
        <div><p class="eyebrow">Ready to sell?</p><h2>Your old scrap could be worth something today.</h2><p>Book a convenient doorstep pickup in Delhi-NCR.</p></div>
        <router-link to="/scrap-selling/schedule" class="btn">Schedule a Pickup</router-link>
      </div>
    </section>
  </div>
</template>
