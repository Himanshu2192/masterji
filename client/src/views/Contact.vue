<template>
  <div class="page">
    <h1>Contact Us</h1>
    <p class="lead">
      Have a question about any of our services? Send us a message and we'll get
      back to you.
    </p>

    <form class="contact-form" @submit.prevent="submitForm">
      <label for="name">Name</label>
      <input id="name" v-model="form.name" type="text" placeholder="Your Name" required />

      <label for="email">Email</label>
      <input id="email" v-model="form.email" type="email" placeholder="Your Email" required />

      <label for="phone">Phone</label>
      <input id="phone" v-model="form.phone" type="tel" placeholder="Phone Number" />

      <label for="company">Company or Organisation <span>(optional)</span></label>
      <input id="company" v-model="form.company" type="text" placeholder="Company or Organisation" />

      <label for="service">Service</label>
      <select id="service" v-model="form.service">
        <option value="">Select a Service (optional)</option>
        <option value="tour_travel">Tour &amp; Travel Bookings</option>
        <option value="solar_panel">Solar Panel Installation</option>
        <option value="interior_design">Interior Design</option>
        <option value="touring_services">Touring Services</option>
        <option value="scrap_selling">Scrap Selling</option>
      </select>

      <label for="preferred-contact">Preferred contact method</label>
      <select id="preferred-contact" v-model="form.preferred_contact">
        <option value="">No preference</option>
        <option value="phone">Phone</option>
        <option value="email">Email</option>
        <option value="whatsapp">WhatsApp</option>
      </select>

      <label for="budget-range">Approximate budget <span>(optional)</span></label>
      <select id="budget-range" v-model="form.budget_range">
        <option value="">Prefer to discuss</option>
        <option value="under_25000">Under ₹25,000</option>
        <option value="25000_100000">₹25,000 – ₹1,00,000</option>
        <option value="100000_500000">₹1,00,000 – ₹5,00,000</option>
        <option value="over_500000">Over ₹5,00,000</option>
      </select>

      <label for="timeline">When do you need this?</label>
      <select id="timeline" v-model="form.timeline">
        <option value="">Not decided yet</option>
        <option value="urgent">Within 2 weeks</option>
        <option value="soon">Within 1–3 months</option>
        <option value="later">More than 3 months</option>
      </select>

      <template v-if="form.service === 'scrap_selling'">
        <label for="pickup-address">Pickup address</label>
        <textarea id="pickup-address" v-model="form.pickup_address" rows="3" placeholder="House/office address and area"></textarea>

        <label for="pickup-date">Preferred pickup date</label>
        <input id="pickup-date" v-model="form.pickup_date" type="date" />

        <label for="pickup-time">Preferred pickup time</label>
        <select id="pickup-time" v-model="form.pickup_time">
          <option value="">Any available time</option>
          <option value="morning">Morning</option>
          <option value="afternoon">Afternoon</option>
          <option value="evening">Evening</option>
        </select>
      </template>

      <label for="message">Message</label>
      <textarea id="message" v-model="form.message" rows="5" placeholder="Your Message" required></textarea>

      <button type="submit" class="btn" :disabled="submitting">
        {{ submitting ? "Sending..." : "Send Message" }}
      </button>
    </form>

    <p v-if="status === 'success'" style="color: green; margin-top: 16px;">
      Thanks! Your message has been sent.
    </p>
    <p v-if="status === 'error'" style="color: crimson; margin-top: 16px;">
      Something went wrong. Please try again.
    </p>

    <div style="margin-top: 40px;">
      <h2 style="font-size: 1.1rem;">Reach Us Directly</h2>
      <p>Email: info@masterjiconsultancy.com</p>
      <p>Phone: <a href="tel:+919560806929">+91 95608 06929</a></p>
    </div>
  </div>
</template>

<script setup>
import { reactive, ref } from "vue";
import { api } from "../api";
import { usePageSeo } from "../composables/usePageSeo";
import { SITE_NAME, SITE_URL } from "../seo";

const form = reactive({
  name: "",
  email: "",
  phone: "",
  company: "",
  service: "",
  preferred_contact: "",
  budget_range: "",
  timeline: "",
  pickup_address: "",
  pickup_date: "",
  pickup_time: "",
  message: ""
});

const status = ref(null);
const submitting = ref(false);

async function submitForm() {
  status.value = null;
  submitting.value = true;
  try {
    await api.post("/contact", { ...form });
    status.value = "success";
    Object.assign(form, {
      name: "",
      email: "",
      phone: "",
      company: "",
      service: "",
      preferred_contact: "",
      budget_range: "",
      timeline: "",
      pickup_address: "",
      pickup_date: "",
      pickup_time: "",
      message: ""
    });
  } catch (err) {
    status.value = "error";
  } finally {
    submitting.value = false;
  }
}

usePageSeo({
  schema: {
    "@context": "https://schema.org",
    "@type": "ContactPage",
    name: `Contact ${SITE_NAME}`,
    url: `${SITE_URL}/contact`
  }
});
</script>
