<script setup>
import { usePageSeo } from "../composables/usePageSeo";
import { SITE_NAME, SITE_URL } from "../seo";

const vehicles = [
  { name: "9-Seater Traveller", capacity: "9+1 / 9+2", rate: "₹20/km", driver: "₹500/day", image: "https://images.unsplash.com/photo-1544620347-c4fd4a3d5957?auto=format&fit=crop&w=900&q=80", features: "AC · push-back seats · charging · luggage space" },
  { name: "12-Seater Traveller", capacity: "12+1 / 12+2", rate: "₹22/km", driver: "₹500/day", image: "https://images.unsplash.com/photo-1549317661-bd32c8ce0db2?auto=format&fit=crop&w=900&q=80", features: "AC · comfortable group seating · music · luggage space" },
  { name: "16-Seater Traveller", capacity: "16+2", rate: "₹22/km", driver: "₹500/day", image: "https://images.unsplash.com/photo-1570125909232-eb263c188f7e?auto=format&fit=crop&w=900&q=80", features: "AC · push-back seats · charging · group luggage" },
  { name: "18-Seater Traveller", capacity: "18+2", rate: "₹23/km", driver: "₹500/day", image: "https://images.unsplash.com/photo-1544620347-c4fd4a3d5957?auto=format&fit=crop&w=900&q=80", features: "AC · spacious seating · music · luggage carrier" },
  { name: "20-Seater Traveller", capacity: "20+2", rate: "₹24/km", driver: "₹500/day", image: "https://images.unsplash.com/photo-1570125909517-53cb21c84f34?auto=format&fit=crop&w=900&q=80", features: "AC · push-back seats · charging · luggage space" },
  { name: "26-Seater Traveller", capacity: "24+2 / up to 26", rate: "₹24/km", driver: "₹500/day", image: "https://images.unsplash.com/photo-1570125909232-eb263c188f7e?auto=format&fit=crop&w=900&q=80", features: "AC · large-group seating · music · luggage carrier" }
];

const packages = [
  { name: "Shimla", duration: "4 days / 3 nights", text: "A flexible hill-station itinerary for families and groups." },
  { name: "Manali", duration: "4 days / 3 nights", text: "Mountain sightseeing, local experiences, and comfortable group travel." },
  { name: "Mussoorie", duration: "4 days / 3 nights", text: "A relaxed Uttarakhand escape with transport and itinerary support." },
  { name: "Honeymoon circuit", duration: "6 days / 5 nights", text: "A romantic Shimla and Manali route planned around your pace." }
];

usePageSeo({
  schema: [
    {
      "@context": "https://schema.org",
      "@type": "Service",
      serviceType: "Tempo Traveller Rental and Tour Packages",
      provider: { "@type": "LocalBusiness", name: SITE_NAME, url: SITE_URL },
      areaServed: "India",
      description: "Chauffeur-driven tempo traveller rentals, custom itineraries, group trips, and tour packages."
    },
    {
      "@context": "https://schema.org",
      "@type": "FAQPage",
      mainEntity: [
        { "@type": "Question", name: "Are drivers included?", acceptedAnswer: { "@type": "Answer", text: "Chauffeur-driven travel is available. Driver charges are shown as an indicative daily amount and confirmed with your quote." } },
        { "@type": "Question", name: "Is there a minimum distance for outstation trips?", acceptedAnswer: { "@type": "Answer", text: "Outstation quotes commonly use a 250 km per day minimum. We confirm the calculation for your route before booking." } },
        { "@type": "Question", name: "Are tolls and taxes included?", acceptedAnswer: { "@type": "Answer", text: "Toll, parking, state taxes, government taxes, and other route charges may be extra and are confirmed in the final quote." } }
      ]
    }
  ]
});
</script>

<template>
  <div class="travel-page">
    <section class="travel-hero">
      <div class="travel-hero-inner">
        <div>
          <p class="eyebrow">Comfortable group travel, planned around you</p>
          <h1>Hire a Tempo Traveller for your next journey.</h1>
          <p>Chauffeur-driven vehicles, custom itineraries, outstation trips, and tour packages for families, friends, corporate groups, and celebrations.</p>
          <div class="travel-actions"><router-link to="/contact" class="btn">Get a Travel Quote</router-link><router-link to="/tour-and-travel/rates" class="travel-outline-btn">View Fleet &amp; Rates</router-link></div>
        </div>
        <img src="https://images.unsplash.com/photo-1544620347-c4fd4a3d5957?auto=format&fit=crop&w=1200&q=85" alt="Group travel vehicle on a road" width="1200" height="800" />
      </div>
    </section>

    <section class="travel-section travel-container">
      <div class="travel-heading"><p class="eyebrow">Our fleet</p><h2>Choose the right vehicle for your group</h2><p>Indicative starting rates help you plan. Availability, route, season, and trip duration affect the final quote.</p></div>
      <div class="vehicle-grid">
        <article v-for="vehicle in vehicles" :key="vehicle.name" class="vehicle-card">
          <img :src="vehicle.image" :alt="vehicle.name" loading="lazy" width="900" height="600" />
          <div class="vehicle-card-body"><h3>{{ vehicle.name }}</h3><p class="vehicle-capacity">{{ vehicle.capacity }} · chauffeur-driven</p><p>{{ vehicle.features }}</p><div class="vehicle-price"><strong>{{ vehicle.rate }}</strong><span>Driver {{ vehicle.driver }}</span></div><router-link to="/contact" class="btn">Enquire</router-link></div>
        </article>
      </div>
      <router-link to="/tour-and-travel/rates" class="text-link">See complete fleet and rate notes →</router-link>
    </section>

    <section class="travel-section travel-container">
      <div class="travel-heading"><p class="eyebrow">Travel your way</p><h2>One-way, round trip, or a complete itinerary</h2></div>
      <div class="travel-option-grid">
        <article><span>🧭</span><h3>Custom outstation trips</h3><p>Choose your route, stops, vehicle, and travel dates. We help shape a practical itinerary.</p></article>
        <article><span>👨‍👩‍👧‍👦</span><h3>Family and group travel</h3><p>Keep your group together with comfortable seating, luggage space, and a professional driver.</p></article>
        <article><span>🎉</span><h3>Weddings and events</h3><p>Coordinate guest transport, airport transfers, local movement, and event-day logistics.</p></article>
        <article><span>💼</span><h3>Corporate travel</h3><p>Plan employee outings, offsites, conferences, and multi-day group movement.</p></article>
      </div>
    </section>

    <section class="travel-section travel-container">
      <div class="travel-heading"><p class="eyebrow">Popular ideas</p><h2>Start with a destination, then make it yours</h2></div>
      <div class="package-grid"><article v-for="pkg in packages" :key="pkg.name" class="package-card"><h3>{{ pkg.name }}</h3><strong>{{ pkg.duration }}</strong><p>{{ pkg.text }}</p><router-link to="/contact" class="text-link">Plan this trip →</router-link></article></div>
    </section>

    <section class="travel-section travel-container">
      <div class="travel-info-grid">
        <article><p class="eyebrow">What to expect</p><h2>Clear quote, comfortable journey</h2><ul><li>Vehicle and seating matched to your group</li><li>Professional chauffeur-driven travel</li><li>Flexible one-way and round-trip planning</li><li>Support for short and multi-day itineraries</li></ul></article>
        <article class="travel-charge-box"><h3>Important rate notes</h3><p>Outstation calculations may use a 250 km per day minimum. Toll, parking, state tax, government taxes, and other route charges may be extra. Rates and vehicles are subject to availability and are confirmed before booking.</p><router-link to="/tour-and-travel/rates" class="text-link">Read pricing notes →</router-link></article>
      </div>
    </section>

    <section class="travel-cta"><div class="travel-container travel-cta-inner"><div><p class="eyebrow">Planning a trip?</p><h2>Tell us your route, dates, and group size.</h2><p>We will recommend a vehicle and prepare a customised quote.</p></div><router-link to="/contact" class="btn">Request a Quote</router-link></div></section>
  </div>
</template>
