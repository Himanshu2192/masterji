<script setup>
import { usePageSeo } from "../composables/usePageSeo";
import { SITE_NAME, SITE_URL } from "../seo";

const props = defineProps({
  type: { type: String, required: true }
});

const guides = {
  materials: {
    title: "Accepted Scrap Materials",
    eyebrow: "Know what you can sell",
    description: "A simple guide to common recyclable items collected from homes, offices, shops, and societies.",
    sections: [
      ["Paper and cardboard", "Newspapers, magazines, books, office paper, cartons, packaging, and files."],
      ["Metals", "Iron, steel, aluminium, copper, brass, utensils, wires, and selected hardware."],
      ["Electronics and appliances", "Old computers, phones, printers, cables, small appliances, and other e-waste for assessment."],
      ["Household items", "Plastic containers, furniture, household goods, and other items that may be reusable or recyclable."]
    ]
  },
  pickup: {
    title: "How Scrap Pickup Works",
    eyebrow: "Simple collection process",
    description: "Share a few details and we will help you understand the next step before arranging collection.",
    sections: [
      ["1. Send the details", "Tell us your location, the type of scrap, approximate quantity, and preferred pickup time."],
      ["2. Get an estimate", "We review the material mix and explain whether the request is best handled as a weighed collection or a custom quote."],
      ["3. Prepare the material", "Keep items accessible and separate fragile electronics or sharp materials where possible."],
      ["4. Complete collection", "The material is checked, weighed where applicable, and directed for reuse, sorting, or recycling."]
    ]
  },
  prices: {
    title: "Scrap Prices and Estimates",
    eyebrow: "Transparent expectations",
    description: "Scrap prices change with market rates and material quality, so online figures should be treated as guidance rather than a guarantee.",
    sections: [
      ["Material type matters", "Paper, iron, aluminium, copper, plastic, and electronics are valued differently."],
      ["Weight and quantity matter", "Larger quantities can make collection more practical, especially for offices and societies."],
      ["Condition matters", "Clean, sorted material is easier to assess. Mixed or damaged items may need a separate review."],
      ["Final quote at confirmation", "Share photos or a short list for a more useful estimate before scheduling a pickup."]
    ]
  }
};

const guide = guides[props.type];
usePageSeo({
  title: `${guide.title} | ${SITE_NAME}`,
  description: guide.description,
  schema: {
    "@context": "https://schema.org",
    "@type": "WebPage",
    name: guide.title,
    url: `${SITE_URL}/scrap-selling/${props.type === "materials" ? "accepted-materials" : props.type === "pickup" ? "how-it-works" : "prices"}`
  }
});
</script>

<template>
  <div class="page guide-page">
    <p class="eyebrow">{{ guide.eyebrow }}</p>
    <h1>{{ guide.title }}</h1>
    <p class="lead">{{ guide.description }}</p>
    <div class="guide-content">
      <article v-for="section in guide.sections" :key="section[0]" class="card">
        <h2>{{ section[0] }}</h2>
        <p>{{ section[1] }}</p>
      </article>
    </div>
    <router-link to="/contact" class="btn">Request a Scrap Pickup</router-link>
    <p class="back-link"><router-link to="/scrap-selling">Back to Scrap Selling</router-link></p>
  </div>
</template>
