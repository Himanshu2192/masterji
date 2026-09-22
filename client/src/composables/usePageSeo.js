import { useHead } from "@vueuse/head";
import { useRoute } from "vue-router";
import { SITE_NAME, DEFAULT_OG_IMAGE, absoluteUrl } from "../seo";

/**
 * Applies unique title, meta description, canonical tag, Open Graph /
 * Twitter card tags, robots directive, and optional JSON-LD structured
 * data for the current route. Call once per page component.
 *
 * @param {Object} [options]
 * @param {string} [options.title]       Overrides route meta title.
 * @param {string} [options.description] Overrides route meta description.
 * @param {string} [options.image]       Overrides the default OG image.
 * @param {Object|Object[]} [options.schema] JSON-LD object(s) to inject.
 */
export function usePageSeo(options = {}) {
  const route = useRoute();

  const title = options.title || route.meta.title || SITE_NAME;
  const description = options.description || route.meta.description || "";
  const canonical = absoluteUrl(route.path);
  const image = options.image || DEFAULT_OG_IMAGE;
  const noindex = Boolean(route.meta.noindex);

  const schemas = options.schema
    ? Array.isArray(options.schema)
      ? options.schema
      : [options.schema]
    : [];

  useHead({
    title,
    meta: [
      { name: "description", content: description },
      {
        name: "robots",
        content: noindex ? "noindex, nofollow" : "index, follow"
      },
      { property: "og:site_name", content: SITE_NAME },
      { property: "og:title", content: title },
      { property: "og:description", content: description },
      { property: "og:image", content: image },
      { property: "og:url", content: canonical },
      { property: "og:type", content: "website" },
      { name: "twitter:card", content: "summary_large_image" },
      { name: "twitter:title", content: title },
      { name: "twitter:description", content: description },
      { name: "twitter:image", content: image }
    ],
    link: [{ rel: "canonical", href: canonical }],
    script: schemas.map((schema) => ({
      type: "application/ld+json",
      children: JSON.stringify(schema)
    }))
  });
}
