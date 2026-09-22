<template>
  <footer class="site-footer">
    <div class="footer-inner">
      <div class="footer-col">
        <h3>Masterji Consultancy</h3>
        <p>Tour &amp; Travel · Solar Panel Installation · Interior Design · Touring Services</p>
      </div>

      <div class="footer-col">
        <h4>Contact</h4>
        <router-link to="/contact">Get in touch</router-link>
        <p>Email: info@masterjiconsultancy.com</p>
        <p>Phone: <a href="tel:+919560806929">+91 95608 06929</a></p>
      </div>

      <div class="footer-col">
        <h4>Legal</h4>
        <router-link to="/terms-and-conditions">Terms &amp; Conditions</router-link>
      </div>
    </div>

    <div class="footer-bottom">
      &copy; {{ year }} Masterji Consultancy. All rights reserved.
    </div>
  </footer>
</template>

<script setup>
const year = new Date().getFullYear();
</script>

<style scoped>
.site-footer {
  background: #0f2a3d;
  color: #cfd8dd;
  margin-top: 60px;
}
.footer-inner {
  max-width: 1200px;
  margin: 0 auto;
  padding: 40px 24px 20px;
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 24px;
}
.footer-col h3,
.footer-col h4 {
  color: #fff;
  margin-bottom: 10px;
}
.footer-col a {
  color: #f2a71b;
  text-decoration: none;
  display: inline-block;
  margin-bottom: 6px;
}
.footer-bottom {
  border-top: 1px solid rgba(255, 255, 255, 0.1);
  text-align: center;
  padding: 14px;
  font-size: 0.85rem;
}

@media (max-width: 700px) {
  .footer-inner {
    grid-template-columns: 1fr;
  }
}
</style>
