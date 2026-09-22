// Central SEO constants. Update SITE_URL once the real domain is connected.
export const SITE_NAME = "Masterji Consultancy";

// TODO: replace with the real production domain once connected (item: "connect a custom domain").
export const SITE_URL = "https://www.masterjiconsultancy.com";

export const DEFAULT_DESCRIPTION =
  "Masterji Consultancy offers tour & travel bookings, solar panel installation, interior design, touring services, and scrap collection.";

export const DEFAULT_OG_IMAGE = `${SITE_URL}/og-image.png`;

export function absoluteUrl(path) {
  if (!path) return SITE_URL;
  return `${SITE_URL}${path.startsWith("/") ? path : "/" + path}`;
}
