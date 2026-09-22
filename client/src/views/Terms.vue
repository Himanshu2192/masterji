<template>
  <div class="page">
    <h1>Terms &amp; Conditions</h1>
    <p class="lead">Last updated: {{ today }}</p>

    <div class="legal-copy">
      <h2>1. General</h2>
      <p>
        By using Masterji Consultancy's website and services (Tour &amp; Travel
        Bookings, Solar Panel Installation, Interior Design, and Touring Services),
        you agree to the terms outlined here.
        <!-- TODO: replace this placeholder copy with your finalized legal terms -->
      </p>

      <h2>2. Bookings &amp; Payments</h2>
      <p>
        Booking confirmations, cancellation policies and payment terms for each
        service will be detailed here.
      </p>

      <h2>3. Liability</h2>
      <p>
        Masterji Consultancy's liability in connection with any service provided
        is limited as described here.
      </p>

      <h2>4. Privacy</h2>
      <p>
        Information on how customer data submitted through this website (e.g. via
        the contact form) is stored and used will be detailed here.
      </p>

      <h2>5. Contact</h2>
      <p>
        Questions about these terms can be sent via the
        <router-link to="/contact">contact page</router-link>.
      </p>
    </div>
  </div>
</template>

<script setup>
import { usePageSeo } from "../composables/usePageSeo";

const today = new Date().toLocaleDateString();

usePageSeo();
</script>
