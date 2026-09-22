<template>
  <div>
    <section class="hero">
      <div class="hero-copy">
        <p class="eyebrow">Practical support for your next project</p>
        <h1>Plan better. Build better. Travel better.</h1>
        <p>Masterji Consultancy brings travel planning, solar solutions, interior design, and local experiences together in one dependable place.</p>
        <router-link to="/contact" class="btn">Get in Touch</router-link>
      </div>
      <img
        class="hero-image"
        src="https://images.unsplash.com/photo-1488646953014-85cb44e25828?auto=format&fit=crop&w=1000&q=80"
        alt="Traveller looking across a mountain landscape"
        width="1000"
        height="700"
      />
    </section>

    <div class="page">
      <h2>Our Services</h2>
      <p class="lead">Choose a service to learn more.</p>

      <div class="card-grid">
        <article class="card service-card" v-for="s in services" :key="s.to">
          <img :src="s.image" :alt="s.imageAlt" loading="lazy" width="800" height="500" />
          <h3>{{ s.title }}</h3>
          <p>{{ s.desc }}</p>
          <router-link :to="s.to" class="btn">Explore</router-link>
        </article>
      </div>
    </div>
  </div>
</template>

<script setup>
import { usePageSeo } from "../composables/usePageSeo";
import { SITE_NAME, SITE_URL, DEFAULT_OG_IMAGE } from "../seo";

const services = [
  {
    title: "Tour & Travel Bookings",
    desc: "Domestic and international trip planning, flights, hotels and packages.",
    to: "/tour-and-travel",
    image: "https://images.unsplash.com/photo-1488646953014-85cb44e25828?auto=format&fit=crop&w=800&q=75",
    imageAlt: "Mountain travel destination"
  },
  {
    title: "Solar Panel Installation",
    desc: "Residential and commercial solar setup, consultation and maintenance.",
    to: "/solar-panel-installation",
    image: "https://images.unsplash.com/photo-1509391366360-2e959784a276?auto=format&fit=crop&w=800&q=75",
    imageAlt: "Solar panels on a rooftop"
  },
  {
    title: "Interior Design",
    desc: "End-to-end interior design for homes and offices.",
    to: "/interior-design",
    image: "https://images.unsplash.com/photo-1618221195710-dd6b41faaea6?auto=format&fit=crop&w=800&q=75",
    imageAlt: "Bright modern interior"
  },
  {
    title: "Touring Services",
    desc: "Guided local tours, itineraries and travel logistics.",
    to: "/touring-services",
    image: "https://images.unsplash.com/photo-1500530855697-b586d89ba3ee?auto=format&fit=crop&w=800&q=75",
    imageAlt: "Scenic guided tour destination"
  },
  {
    title: "Scrap Selling",
    desc: "Convenient collection for paper, metal, electronics, and household scrap.",
    to: "/scrap-selling",
    image: "https://images.unsplash.com/photo-1532996122724-e3c354a0b15b?auto=format&fit=crop&w=800&q=75",
    imageAlt: "Sorted recyclable materials"
  }
];

// LocalBusiness structured data.
usePageSeo({
  schema: [
    {
      "@context": "https://schema.org",
      "@type": "LocalBusiness",
      name: SITE_NAME,
      url: SITE_URL,
      image: DEFAULT_OG_IMAGE,
      telephone: "+919560806929",
      areaServed: "IN"
    },
    {
      "@context": "https://schema.org",
      "@type": "Organization",
      name: SITE_NAME,
      url: SITE_URL,
      logo: `${SITE_URL}/favicon.svg`
    }
  ]
});
</script>
