# Masterji Consultancy Website

Services: Tour & Travel Bookings · Solar Panel Installation · Interior Design · Touring Services

Stack: **Vite + Vue.js** (client) · **Flask** (server) · **PostgreSQL** (database)

## Project structure

```
masterji/
├── client/      # Vite + Vue 3 frontend
├── server/      # Flask REST API
└── database/    # PostgreSQL schema & seed data
```

## 1. Database setup (PostgreSQL)

```bash
createdb masterji_db
psql -d masterji_db -f database/schema.sql
psql -d masterji_db -f database/seed.sql
```

Or let Flask create the tables for you (see below), then run `seed.sql` to add the four services.

## 2. Backend setup (Flask)

```bash
cd server
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt

# Set your DB connection (or edit config.py directly)
export DB_USER=postgres
export DB_PASSWORD=hk219287@
export DB_HOST=localhost
export DB_PORT=5432
export DB_NAME=masterji_db

python app.py
```

The API runs at `http://localhost:5000`. Key endpoints:

- `GET  /api/health`
- `GET  /api/services/`
- `GET  /api/services/<slug>`
- `POST /api/contact/`
- `GET  /api/contact/`

## 3. Frontend setup (Vite + Vue)

```bash
cd client
npm install
npm run dev
```

The site runs at `http://localhost:5173` and proxies `/api` requests to the Flask server.

## Pages

- Home (`/`)
- Tour & Travel Bookings (`/tour-and-travel`)
- Solar Panel Installation (`/solar-panel-installation`)
- Interior Design (`/interior-design`)
- Touring Services (`/touring-services`)
- Contact (`/contact`)
- Terms & Conditions (`/terms-and-conditions`)

The header has a **Services** dropdown linking to each of the four services, and the footer has **Contact** and **Terms & Conditions** links.

## SEO / technical setup

This project now includes: per-page titles/descriptions/canonicals (via `@vueuse/head`), Open Graph + Twitter card tags, JSON-LD structured data (LocalBusiness, Organization, Service, ContactPage, BreadcrumbList), breadcrumbs, a custom 404 page, `sitemap.xml` / `robots.txt`, a favicon, an og-image, automatic image compression at build time, disabled production source maps, and a Flask-side HTTPS/security-header safety net.

**Run `npm install` again** in `client/` to pick up the new dependencies (`@vueuse/head`, `vite-plugin-image-optimizer`).

See **`docs/SEO-NEXT-STEPS.md`** for the full checklist of what's done in code vs. what still needs your domain/hosting/Search Console/marketing action (things like connecting a real domain, verifying Search Console, and backlink outreach can't be done by editing code).

## Deploying to Vercel

This is a monorepo, so it deploys as **two separate Vercel projects** pointing at the same GitHub repo, plus a managed Postgres database.

### 1. Database (pick one)

Any managed Postgres works — Vercel Postgres (built on Neon), Neon directly, Supabase, or Render Postgres. Create one and copy its **pooled** connection string (serverless functions open many short-lived connections, so a pooled string avoids exhausting Postgres' connection limit).

### 2. Backend project (Flask, as Python serverless functions)

1. In Vercel: **Add New → Project**, import this repo, set **Root Directory** to `server`.
2. Framework preset: "Other" (Vercel will pick up `server/vercel.json` and `server/api/index.py` automatically).
3. Add Environment Variables (copy from `server/.env.example`): `DATABASE_URL`, `SECRET_KEY`, `ALLOWED_ORIGINS` (set once you know the frontend's URL — see step 4).
4. Deploy. Note the resulting URL, e.g. `https://masterji-server.vercel.app`.
5. One-time only, from your own machine (not on Vercel — serverless functions don't run this automatically):
   ```bash
   cd server
   pip install -r requirements.txt
   DATABASE_URL="<your pooled connection string>" python scripts/init_db.py
   DATABASE_URL="<your pooled connection string>" python scripts/seed_db.py
   ```

### 3. Frontend project (Vite + Vue)

1. **Add New → Project** again on the same repo, set **Root Directory** to `client`.
2. Framework preset: "Vite" (auto-detected). Build command `npm run build`, output directory `dist` (defaults are correct).
3. Add Environment Variable `VITE_API_URL` = `https://masterji-server.vercel.app/api` (the backend URL from step 2, with `/api` appended).
4. Deploy. `client/vercel.json` is already set up so client-side routes (e.g. `/tour-and-travel`) work on direct load/refresh, not just in-app navigation.

### 4. Wire the two together

- Go back to the **backend** project's env vars and set `ALLOWED_ORIGINS` to the frontend's real URL (and its Vercel preview-deployment URL pattern, comma-separated), then redeploy the backend so CORS allows it.
- Update `client/src/seo.js` (`SITE_URL`), `client/public/sitemap.xml`, and `client/public/robots.txt` to your real frontend domain, and redeploy the frontend.

### 5. Custom domain

Add your domain under the **frontend** project's Settings → Domains. Vercel issues and renews the HTTPS certificate automatically — no action needed beyond DNS. If you want the backend on a subdomain (e.g. `api.yourdomain.com`), add the domain to the backend project the same way.

### Good to know about running Flask this way

- Serverless functions are stateless between requests — fine for this app since there's no in-memory state, but background jobs or scheduled tasks won't work here without Vercel Cron or a separate worker.
- Cold starts add latency to the first request after idle time.
- The Hobby plan caps execution at 10s per request (60s on Pro) — plenty for this API, but worth knowing if you add slower endpoints later.
- If this ever becomes a limitation, the backend can be moved to Render or Railway instead (both run Flask as a normal long-lived process) while keeping the frontend on Vercel — only `VITE_API_URL` needs to change.
