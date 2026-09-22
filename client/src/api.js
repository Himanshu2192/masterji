import axios from "axios";

// In local dev, VITE_API_URL is unset and requests go to "/api", which
// vite.config.js proxies to the local Flask server.
// In production on Vercel, set VITE_API_URL (in the Vercel project's
// Environment Variables) to your deployed backend's URL, e.g.
// https://masterji-server.vercel.app/api
const baseURL = import.meta.env.VITE_API_URL || "/api";

export const api = axios.create({ baseURL });
