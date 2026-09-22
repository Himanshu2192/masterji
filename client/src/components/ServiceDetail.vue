<template>
  <div class="page service-page">
    <section class="service-banner" :style="{ backgroundImage: `url(${service.image})` }">
      <div class="service-banner-overlay">
        <p class="eyebrow">{{ service.eyebrow }}</p>
        <h1>{{ service.title }}</h1>
        <p>{{ service.intro }}</p>
        <router-link to="/contact" class="btn">Get a Free Quote</router-link>
      </div>
    </section>

    <section class="service-section">
      <div class="section-heading">
        <p class="eyebrow">How we can help</p>
        <h2>Simple support, tailored to your needs</h2>
        <p>Choose the option that fits your plans and we will help you take the next step with clear guidance.</p>
      </div>
      <div class="service-offerings">
        <article v-for="item in service.offerings" :key="item.title" class="service-offering card">
          <span class="service-icon" aria-hidden="true">{{ item.icon }}</span>
          <h3>{{ item.title }}</h3>
          <p>{{ item.description }}</p>
        </article>
      </div>
    </section>

    <section v-if="service.highlights" class="service-section scope-section">
      <div class="section-heading">
        <p class="eyebrow">Plan your project</p>
        <h2>What can we help you improve?</h2>
        <p>Start with one area or plan a complete transformation. We help you prioritise the work that will make the biggest difference to your space.</p>
      </div>
      <div class="scope-grid">
        <article v-for="item in service.highlights" :key="item.title" class="scope-item">
          <div class="scope-icon" aria-hidden="true">{{ item.icon }}</div>
          <div>
            <h3>{{ item.title }}</h3>
            <p>{{ item.description }}</p>
          </div>
        </article>
      </div>
    </section>

    <section class="service-section pricing-section">
      <div class="section-heading">
        <p class="eyebrow">Indicative pricing</p>
        <h2>Choose a starting point</h2>
        <p>These guide prices help with planning. We confirm the final quote after understanding your dates, scope, materials, and preferences.</p>
      </div>
      <div class="pricing-grid">
        <article v-for="plan in service.pricing" :key="plan.name" class="pricing-card" :class="{ featured: plan.featured }">
          <span v-if="plan.featured" class="pricing-badge">Most popular</span>
          <h3>{{ plan.name }}</h3>
          <p class="pricing-description">{{ plan.description }}</p>
          <p class="pricing-amount">{{ plan.price }}</p>
          <p class="pricing-note">Starting from</p>
          <router-link to="/contact" class="btn">Ask About This</router-link>
        </article>
      </div>
    </section>

    <section class="service-section process-section">
      <div class="section-heading">
        <p class="eyebrow">Our approach</p>
        <h2>A clear process from first conversation to completion</h2>
      </div>
      <ol class="process-list">
        <li v-for="(step, index) in service.process" :key="step.title">
          <span class="process-number">{{ index + 1 }}</span>
          <div>
            <h3>{{ step.title }}</h3>
            <p>{{ step.description }}</p>
          </div>
        </li>
      </ol>
    </section>

    <section class="service-section faq-section">
      <div class="section-heading">
        <p class="eyebrow">Good to know</p>
        <h2>Frequently asked questions</h2>
      </div>
      <div class="faq-list">
        <details v-for="faq in service.faqs" :key="faq.question" class="faq-item">
          <summary>{{ faq.question }}<span aria-hidden="true">+</span></summary>
          <p>{{ faq.answer }}</p>
        </details>
      </div>
    </section>

    <section class="service-cta">
      <div>
        <p class="eyebrow">Ready when you are</p>
        <h2>{{ service.ctaTitle }}</h2>
        <p>{{ service.ctaText }}</p>
      </div>
      <router-link to="/contact" class="btn">Talk to Us</router-link>
    </section>

    <RelatedServices :current="service.current" />
  </div>
</template>

<script setup>
import RelatedServices from "./RelatedServices.vue";

defineProps({
  service: { type: Object, required: true }
});
</script>
