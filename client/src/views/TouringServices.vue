<script setup>
import ServiceDetail from "../components/ServiceDetail.vue";
import { usePageSeo } from "../composables/usePageSeo";
import { SITE_NAME, SITE_URL } from "../seo";

const service = {
  current: "touring-services",
  eyebrow: "See more, stress less",
  title: "Touring Services",
  intro: "Enjoy local and regional experiences with thoughtful itinerary planning, guided sightseeing, and the on-ground logistics that keep a tour moving.",
  image: "https://images.unsplash.com/photo-1500530855697-b586d89ba3ee?auto=format&fit=crop&w=1400&q=85",
  offerings: [
    { icon: "📍", title: "Guided city tours", description: "Explore cultural, historical, and local highlights with an itinerary built around your pace." },
    { icon: "👥", title: "Group and corporate tours", description: "Coordinate transport, timing, and activities for teams, families, and larger groups." },
    { icon: "🥾", title: "Custom experiences", description: "Plan relaxed sightseeing, adventure outings, or a mix of experiences for your group." }
  ],
  pricing: [
    { name: "Local half-day", description: "A guided local experience for a small group.", price: "₹2,499", featured: false },
    { name: "Full-day tour", description: "A planned day of sightseeing with coordinated logistics.", price: "₹5,999", featured: true },
    { name: "Group outing", description: "Custom planning for families, teams, and larger groups.", price: "₹12,999", featured: false }
  ],
  process: [
    { title: "Choose the experience", description: "Tell us where you want to go, who is travelling, and the kind of day or trip you prefer." },
    { title: "Build the itinerary", description: "We arrange a balanced route with realistic timings, stops, transport, and local details." },
    { title: "Enjoy the day", description: "With the plan and logistics in place, you can focus on the people and places around you." }
  ],
  faqs: [
    { question: "Can tours be customised for our group?", answer: "Yes. We can adjust the route, pace, stops, and activities for families, friends, corporate groups, or special occasions." },
    { question: "Do you arrange transport as well?", answer: "We can help coordinate the travel logistics needed for your itinerary and group size." },
    { question: "Can you plan a one-day local tour?", answer: "Yes. One-day city, sightseeing, and nearby destination plans are welcome." }
  ],
  ctaTitle: "Ready to plan your next outing?",
  ctaText: "Tell us about your group and the experience you want to create."
};

usePageSeo({
  schema: {
    "@context": "https://schema.org",
    "@type": "Service",
    serviceType: "Touring Services",
    provider: { "@type": "LocalBusiness", name: SITE_NAME, url: SITE_URL },
    areaServed: "IN",
    description: service.intro
  }
});
</script>

<template>
  <ServiceDetail :service="service" />
</template>
