# SEO / Technical Checklist — What's Done vs. What Needs You

This tracks the full improvement list you asked for. Most items are now implemented
in code. A handful genuinely can't be done by editing code — they need a real
domain, hosting account, Google account, or human outreach. Those are marked
**[MANUAL]** below with the steps to do them yourself.

## ✅ Implemented in code

| Item | Where |
|---|---|
| sitemap.xml | `client/public/sitemap.xml` |
| robots.txt (with sitemap reference) | `client/public/robots.txt` |
| No noindex tags by default | `usePageSeo.js` — only the 404 route sets `noindex` |
| Canonical tag per page | `usePageSeo.js` → `<link rel="canonical">` |
| Unique meta title per page | `router/index.js` `meta.title` per route |
| Unique meta description per page | `router/index.js` `meta.description` per route |
| One `<h1>` per page, fixed heading order (h1→h2→h3) | All files in `client/src/views/` |
| Alt text on images | Header logo (`AppHeader.vue`); note below on photos |
| Schema.org structured data (JSON-LD) | `Home.vue` (LocalBusiness + Organization), each service page (Service), `Contact.vue` (ContactPage), `Breadcrumbs.vue` (BreadcrumbList) |
| Local business schema | `Home.vue` — **fill in the real phone/address, see below** |
| Internal links | `RelatedServices.vue` on every service page + breadcrumbs |
| Broken links | Audited — all nav/footer/router-links point to valid routes |
| Compress images | `vite-plugin-image-optimizer` wired into `vite.config.js`; run `npm install` to pull it in. `og-image.png` was generated and saved with PNG optimization on |
| Core Web Vitals | Routes are now lazy-loaded (code-splitting), `preconnect` added, no client-side render-blocking work added |
| Mobile responsiveness | Extra breakpoints added in `main.css`, form labels/select styled, header nav already collapses on mobile |
| Enforce HTTPS | Flask `enforce_https()` + HSTS header in `server/app.py` (backup only — see MANUAL below) |
| Clean URL slugs | Already kebab-case and descriptive (`/tour-and-travel`, etc.) — left as-is |
| og:image | `client/public/og-image.png` (placeholder — swap for a real branded 1200×630 image later) |
| Custom 404 page | `NotFound.vue` + catch-all route, `noindex` set automatically |
| Favicon | `client/public/favicon.svg` + `favicon.ico` (placeholder "M" mark — swap for your real logo) |
| Breadcrumbs | `Breadcrumbs.vue`, shown on every page except Home, with BreadcrumbList schema |
| Remove production source maps | `vite.config.js` → `build.sourcemap: false` |

## ⚠️ Placeholders you must replace with real data

These are intentionally marked `TODO` so no fake business data accidentally ships:

- `client/src/seo.js` → `SITE_URL` (swap for your real domain once connected)
- `Home.vue` → LocalBusiness schema: `telephone`, `address` fields
- `Contact.vue` / `AppFooter.vue` → the placeholder email/phone shown on the page
- `client/public/og-image.png` → currently an auto-generated placeholder graphic; replace with a real designed image
- `client/public/sitemap.xml`, `robots.txt`, `index.html` → all reference `https://www.masterjiconsultancy.com`; find/replace once your real domain is live

## [MANUAL] Items that need your accounts, not code

**1. Connect a custom domain**
Buy/point your domain's DNS to wherever you deploy the frontend (Vercel, Netlify,
your own server, etc.) and the backend (Render, Railway, a VPS, etc.). Once live,
replace every placeholder URL above.

**2. Enforce HTTPS (real certificate)**
The Flask code above is a safety-net redirect, not a certificate. Real HTTPS
comes from your host: most (Vercel, Netlify, Render, Cloudflare) issue a free
Let's Encrypt certificate automatically once your domain is connected — no
action needed beyond connecting the domain. If you self-host, run Certbot.

**3. Verify Google Search Console**
- Go to [search.google.com/search-console](https://search.google.com/search-console)
- Add your property (the real domain)
- Verify via the HTML meta tag method — paste the code into the placeholder
  `<meta name="google-site-verification" ...>` left commented in `index.html`
- Submit `https://yourdomain.com/sitemap.xml`

**4. Backlink strategy**
This is outreach/marketing work, not something that can be "built" in code.
A starting plan:
- Claim and complete a Google Business Profile (huge for local SEO + LocalBusiness schema trust)
- List the business on relevant directories (JustDial, IndiaMART, Sulekha, local chamber-of-commerce sites)
- Partner with complementary businesses for reciprocal links (hotels/travel agents for the tour side, solar equipment suppliers, furniture/decor brands for interior design)
- Publish a few genuinely useful blog posts (e.g. "Solar panel subsidy guide 2026", "How to plan a first international trip") that other sites naturally want to link to
- Reach out for guest posts on regional travel/home-improvement blogs
- Get listed on any industry association directories relevant to solar installers or interior designers

**5. Real product photography**
Once you have real photos (project photos, team, office), add them with
descriptive `alt` text and let `vite-plugin-image-optimizer` compress them
automatically at build time.

## Bigger architectural note: SPA vs. SEO

This site is currently a client-side rendered Vue SPA. All the per-page titles,
descriptions, canonicals and schema above are applied **in the browser via
JavaScript**. Modern Googlebot generally executes JavaScript and will see this
correctly, but:
- Some other crawlers/social-link previewers (and Googlebot in edge cases) may
  only see the static fallback tags in `index.html`
- First paint / Largest Contentful Paint for Core Web Vitals is slightly slower
  than a pre-rendered page

If you want the strongest possible SEO result, the next step up is adding
**prerendering or SSR** (e.g. migrating to `vite-ssg` or Nuxt) so each route
ships fully-formed HTML. That's a bigger architectural change than a content
edit, so it's flagged here rather than done silently — happy to do it if you want it.
