<script setup>
import ServiceDetail from "../components/ServiceDetail.vue";
import { usePageSeo } from "../composables/usePageSeo";
import { SITE_NAME, SITE_URL } from "../seo";

const service = {
  current: "interior-design",
  eyebrow: "Spaces that work beautifully",
  title: "Interior Design",
  intro: "Create a space that feels like yours, with thoughtful layouts, useful finishes, and design support from the first idea to the final styling.",
  image: "https://images.unsplash.com/photo-1618221195710-dd6b41faaea6?auto=format&fit=crop&w=1400&q=85",
  offerings: [
    { icon: "🏠", title: "Home interiors", description: "Comfortable, practical rooms designed around how your family actually lives." },
    { icon: "💼", title: "Office interiors", description: "Workspaces that balance professional presentation, productivity, and everyday comfort." },
    { icon: "✨", title: "Renovation and styling", description: "Refresh an existing space with improved layouts, finishes, furniture, and decor." }
  ],
  highlights: [
    { icon: "🛋️", title: "Living rooms", description: "Better layouts, lighting, storage, furniture, and finishes for the space everyone uses." },
    { icon: "🍽️", title: "Kitchens and dining", description: "Practical planning for cabinetry, worktops, appliances, lighting, and everyday movement." },
    { icon: "🛏️", title: "Bedrooms", description: "Calm, personal rooms with considered wardrobes, colour, lighting, and storage." },
    { icon: "🚿", title: "Bathrooms and utility areas", description: "Durable finishes and efficient layouts that make compact areas easier to use." }
  ],
  pricing: [
    { name: "Single room", description: "Design direction, layout, colour, material, and furniture planning for one room.", price: "₹25,000", featured: false },
    { name: "2 BHK interiors", description: "Coordinated design support for a complete 2 BHK home, based on selected scope.", price: "₹1,50,000", featured: true },
    { name: "Office design", description: "Functional planning for a small office, including layout, finishes, and workstation needs.", price: "₹75,000", featured: false }
  ],
  process: [
    { title: "Discuss your space", description: "We understand the property, your taste, practical needs, timeline, and approximate budget." },
    { title: "Shape the direction", description: "Layouts, materials, colours, and furniture choices come together into a clear design direction." },
    { title: "Bring it to life", description: "The final details are coordinated so the finished space feels cohesive and considered." }
  ],
  faqs: [
    { question: "Can you help with only one room?", answer: "Yes. We can work on a single room, selected areas, or a complete home or office depending on what you need." },
    { question: "Do you work with existing furniture?", answer: "Where it suits the new plan, we can retain, reposition, or refresh existing pieces instead of replacing everything." },
    { question: "How do we begin?", answer: "Send us a few details about the space and your goals. We can then discuss the right scope for an initial consultation." }
  ],
  ctaTitle: "Have a space that needs a fresh direction?",
  ctaText: "Share your ideas with us and start with a practical design conversation."
};

usePageSeo({
  schema: {
    "@context": "https://schema.org",
    "@type": "Service",
    serviceType: "Interior Design",
    provider: { "@type": "LocalBusiness", name: SITE_NAME, url: SITE_URL },
    areaServed: "IN",
    description: service.intro
  }
});
</script>

<template>
  <ServiceDetail :service="service" />
</template>
