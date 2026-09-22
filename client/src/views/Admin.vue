<template>
  <div class="page admin-page">
    <div v-if="!auth.token" class="admin-login card">
      <p class="eyebrow">Private workspace</p>
      <h1>Admin sign in</h1>
      <p class="lead">Manage enquiries and service records from one place.</p>
      <form class="contact-form" @submit.prevent="login">
        <label for="admin-username">Username</label>
        <input id="admin-username" v-model="loginForm.username" autocomplete="username" required />
        <label for="admin-password">Password</label>
        <input id="admin-password" v-model="loginForm.password" type="password" autocomplete="current-password" required />
        <button class="btn" type="submit" :disabled="loading">{{ loading ? "Signing in..." : "Sign in" }}</button>
      </form>
      <p v-if="error" class="admin-error">{{ error }}</p>
    </div>

    <template v-else>
      <div class="admin-heading">
        <div><p class="eyebrow">Admin workspace</p><h1>Manage your website</h1></div>
        <button class="btn btn-muted" type="button" @click="logout">Sign out</button>
      </div>
      <div class="admin-tabs" role="tablist">
        <button :class="{ active: tab === 'inquiries' }" type="button" @click="tab = 'inquiries'">Enquiries ({{ inquiries.length }})</button>
        <button :class="{ active: tab === 'services' }" type="button" @click="tab = 'services'">Services ({{ services.length }})</button>
      </div>

      <section v-if="tab === 'inquiries'" class="admin-panel">
        <div class="admin-panel-heading"><div><h2>Contact enquiries</h2><p>Update lead status, add notes, or remove a record.</p></div><button class="btn btn-muted" type="button" @click="loadInquiries">Refresh</button></div>
        <div v-if="loading" class="admin-empty">Loading enquiries...</div>
        <div v-else-if="!inquiries.length" class="admin-empty">No enquiries yet.</div>
        <div v-for="inquiry in inquiries" :key="inquiry.id" class="inquiry-card card">
          <div class="inquiry-top"><div><h3>{{ inquiry.name }}</h3><p>{{ inquiry.email }}<span v-if="inquiry.phone"> · {{ inquiry.phone }}</span></p></div><select v-model="inquiry.status" @change="updateInquiry(inquiry)"><option value="new">New</option><option value="contacted">Contacted</option><option value="qualified">Qualified</option><option value="closed">Closed</option></select></div>
          <p class="inquiry-meta">{{ inquiry.service || "General enquiry" }} · {{ formatDate(inquiry.created_at) }}</p>
          <p>{{ inquiry.message }}</p>
          <div v-if="inquiry.pickup_address" class="inquiry-meta">Pickup: {{ inquiry.pickup_address }}<span v-if="inquiry.pickup_date"> · {{ inquiry.pickup_date }}</span></div>
          <textarea v-model="inquiry.internal_notes" rows="2" placeholder="Internal notes" @blur="updateInquiry(inquiry)"></textarea>
          <button class="danger-link" type="button" @click="deleteInquiry(inquiry)">Delete enquiry</button>
        </div>
      </section>

      <section v-else class="admin-panel">
        <div class="admin-panel-heading"><div><h2>Service records</h2><p>These records support the backend service catalogue.</p></div><button class="btn" type="button" @click="startService">Add service</button></div>
        <form v-if="editingService" class="service-editor card" @submit.prevent="saveService">
          <label for="service-slug">Slug</label><input id="service-slug" v-model="editingService.slug" required />
          <label for="service-name">Name</label><input id="service-name" v-model="editingService.name" required />
          <label for="service-description">Description</label><textarea id="service-description" v-model="editingService.description" rows="3"></textarea>
          <div><button class="btn" type="submit">Save service</button><button class="btn btn-muted" type="button" @click="editingService = null">Cancel</button></div>
        </form>
        <div v-for="service in services" :key="service.id" class="service-admin-row card"><div><h3>{{ service.name }}</h3><p>{{ service.slug }} · {{ service.description || "No description" }}</p></div><div><button class="text-button" type="button" @click="editService(service)">Edit</button><button class="danger-link" type="button" @click="deleteService(service)">Delete</button></div></div>
      </section>
      <p v-if="error" class="admin-error">{{ error }}</p>
    </template>
  </div>
</template>

<script setup>
import { onMounted, reactive, ref } from "vue";
import { api } from "../api";
import { usePageSeo } from "../composables/usePageSeo";

const token = localStorage.getItem("masterji_admin_token");
const auth = reactive({ token });
const loginForm = reactive({ username: "", password: "" });
const inquiries = ref([]);
const services = ref([]);
const editingService = ref(null);
const tab = ref("inquiries");
const loading = ref(false);
const error = ref("");

const adminApi = () => ({ headers: { Authorization: `Bearer ${auth.token}` } });

async function login() {
  loading.value = true;
  error.value = "";
  try {
    const response = await api.post("/admin/login", loginForm);
    auth.token = response.data.token;
    localStorage.setItem("masterji_admin_token", auth.token);
    await loadData();
  } catch {
    error.value = "Invalid username or password.";
  } finally {
    loading.value = false;
  }
}

function logout() {
  localStorage.removeItem("masterji_admin_token");
  auth.token = null;
}

async function loadData() {
  await Promise.all([loadInquiries(), loadServices()]);
}
async function loadInquiries() {
  const response = await api.get("/admin/contact-inquiries", adminApi());
  inquiries.value = response.data;
}
async function loadServices() {
  const response = await api.get("/admin/services", adminApi());
  services.value = response.data;
}
async function updateInquiry(inquiry) {
  try {
    await api.patch(`/admin/contact-inquiries/${inquiry.id}`, inquiry, adminApi());
  } catch {
    error.value = "Unable to update this enquiry.";
  }
}
async function deleteInquiry(inquiry) {
  if (!window.confirm(`Delete the enquiry from ${inquiry.name}?`)) return;
  await api.delete(`/admin/contact-inquiries/${inquiry.id}`, adminApi());
  await loadInquiries();
}
function startService() {
  editingService.value = { slug: "", name: "", description: "" };
}
function editService(service) {
  editingService.value = { ...service };
}
async function saveService() {
  const service = editingService.value;
  if (service.id) await api.put(`/admin/services/${service.id}`, service, adminApi());
  else await api.post("/admin/services", service, adminApi());
  editingService.value = null;
  await loadServices();
}
async function deleteService(service) {
  if (!window.confirm(`Delete ${service.name}?`)) return;
  await api.delete(`/admin/services/${service.id}`, adminApi());
  await loadServices();
}
function formatDate(value) {
  return new Date(value).toLocaleString("en-IN", { dateStyle: "medium", timeStyle: "short" });
}

if (auth.token) onMounted(loadData);
usePageSeo({ title: "Admin | Masterji Consultancy", description: "Private administration area.", noindex: true });
</script>
