<script setup>
import ServiceDetail from "../components/ServiceDetail.vue";
import { usePageSeo } from "../composables/usePageSeo";
import { SITE_NAME, SITE_URL } from "../seo";

const service = {
  current: "solar-panel",
  eyebrow: "Smarter energy for everyday life",
  title: "Solar Panel Installation",
  intro: "Move towards cleaner, more reliable energy with a solar solution planned for your home, office, shop, or larger commercial property.",
  image: "https://images.unsplash.com/photo-1509391366360-2e959784a276?auto=format&fit=crop&w=1400&q=85",
  offerings: [
    { icon: "☀️", title: "Residential solar", description: "Rooftop systems planned around your household usage, available space, and long-term goals." },
    { icon: "🏢", title: "Commercial solutions", description: "Solar planning for offices, shops, institutions, and businesses looking to reduce energy costs." },
    { icon: "🔧", title: "Maintenance support", description: "Ongoing checks and annual maintenance support to help your system stay productive." }
  ],
  pricing: [
    { name: "Home starter", description: "Compact rooftop solution for smaller household usage.", price: "₹85,000", featured: false },
    { name: "Home standard", description: "A balanced residential setup for everyday energy needs.", price: "₹1,45,000", featured: true },
    { name: "Business solution", description: "Larger systems planned for shops, offices, and commercial use.", price: "₹3,50,000", featured: false }
  ],
  process: [
    { title: "Understand your usage", description: "We discuss your current consumption, property, roof condition, and expectations." },
    { title: "Plan the system", description: "You receive a practical recommendation for system size, placement, and installation requirements." },
    { title: "Install and support", description: "The installation is coordinated carefully, with guidance for upkeep after handover." }
  ],
  faqs: [
    { question: "Is solar suitable for my property?", answer: "A site assessment can confirm roof space, sunlight, structure, and the system size that makes sense for your usage." },
    { question: "Do you provide maintenance after installation?", answer: "Yes. We can discuss regular servicing and annual maintenance support based on your system and usage." },
    { question: "How much can I save with solar?", answer: "Savings depend on your usage, system size, electricity tariff, sunlight, and available incentives. We can help estimate this after understanding your property." }
  ],
  ctaTitle: "Thinking about solar?",
  ctaText: "Start with a conversation about your property and energy needs."
};

usePageSeo({
  schema: {
    "@context": "https://schema.org",
    "@type": "Service",
    serviceType: "Solar Panel Installation",
    provider: { "@type": "LocalBusiness", name: SITE_NAME, url: SITE_URL },
    areaServed: "IN",
    description: service.intro
  }
});
</script>

<template>
  <ServiceDetail :service="service" />
</template>
