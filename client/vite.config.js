import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";
import { ViteImageOptimizer } from "vite-plugin-image-optimizer";

export default defineConfig({
  plugins: [
    vue(),
    // Automatically compresses any images added to the project at build time.
    // Requires `npm install` to pull in this plugin (and its optional deps like
    // sharp/svgo) — see package.json devDependencies.
    ViteImageOptimizer({
      png: { quality: 80 },
      jpeg: { quality: 80 },
      jpg: { quality: 80 },
      webp: { lossless: false, quality: 80 },
      svg: { multipass: true }
    })
  ],
  build: {
    // Never ship source maps to production (avoids exposing original source).
    sourcemap: false
  },
  server: {
    port: 5173,
    proxy: {
      "/api": {
        target: "http://localhost:5000",
        changeOrigin: true
      }
    }
  }
});
