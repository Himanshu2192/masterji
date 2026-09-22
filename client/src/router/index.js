import { createRouter, createWebHistory } from "vue-router";

const routes = [
  {
    path: "/",
    name: "home",
    component: () => import("../views/Home.vue"),
    meta: {
    title: "Masterji Consultancy | Travel, Solar, Interiors, Scrap Selling",
      description:
        "Masterji Consultancy offers travel, solar, interior design, touring, and scrap collection services under one roof.",
      breadcrumb: "Home"
    }
  },
  {
    path: "/tour-and-travel",
    name: "tour-travel",
    component: () => import("../views/TourTravel.vue"),
    meta: {
      title: "Tour & Travel Bookings | Masterji Consultancy",
      description:
        "Domestic and international trip planning, flights, hotels and custom travel packages from Masterji Consultancy.",
      breadcrumb: "Tour & Travel Bookings"
    }
  },
  {
    path: "/tour-and-travel/rates",
    name: "tour-travel-rates",
    component: () => import("../views/TourTravelRates.vue"),
    meta: {
      title: "Tempo Traveller Fleet and Rates | Masterji Consultancy",
      description: "View indicative tempo traveller capacities, rates, driver charges, and quote conditions.",
      breadcrumb: "Fleet & Rates"
    }
  },
  {
    path: "/solar-panel-installation",
    name: "solar-panel",
    component: () => import("../views/SolarPanel.vue"),
    meta: {
      title: "Solar Panel Installation | Masterji Consultancy",
      description:
        "Residential and commercial solar panel installation, consultation and maintenance from Masterji Consultancy.",
      breadcrumb: "Solar Panel Installation"
    }
  },
  {
    path: "/interior-design",
    name: "interior-design",
    component: () => import("../views/InteriorDesign.vue"),
    meta: {
      title: "Interior Design Services | Masterji Consultancy",
      description:
        "End-to-end interior design for homes and offices, from concept and layout to furnishing and styling.",
      breadcrumb: "Interior Design"
    }
  },
  {
    path: "/touring-services",
    name: "touring-services",
    component: () => import("../views/TouringServices.vue"),
    meta: {
      title: "Touring Services | Masterji Consultancy",
      description:
        "Guided local tours, group logistics and custom touring experiences from Masterji Consultancy.",
      breadcrumb: "Touring Services"
    }
  },
  {
    path: "/scrap-selling",
    name: "scrap-selling",
    component: () => import("../views/ScrapSelling.vue"),
    meta: {
      title: "Scrap Selling and Recycling | Masterji Consultancy",
      description: "Convenient scrap collection and recycling support for homes, offices, shops, and societies.",
      breadcrumb: "Scrap Selling"
    }
  },
  {
    path: "/scrap-selling/accepted-materials",
    name: "scrap-materials",
    component: () => import("../views/ScrapGuide.vue"),
    props: { type: "materials" },
    meta: { title: "Accepted Scrap Materials | Masterji Consultancy", description: "Learn which paper, metal, electronic, and household materials can be reviewed.", breadcrumb: "Accepted Materials" }
  },
  {
    path: "/scrap-selling/rates",
    name: "scrap-rates",
    component: () => import("../views/ScrapRates.vue"),
    meta: { title: "Scrap Rates | Masterji Consultancy", description: "Indicative scrap rates for recyclable materials and appliances.", breadcrumb: "Scrap Rates" }
  },
  {
    path: "/scrap-selling/schedule",
    name: "scrap-schedule",
    component: () => import("../views/ScrapSchedule.vue"),
    meta: { title: "Schedule a Scrap Pickup | Masterji Consultancy", description: "Request a doorstep scrap pickup in Delhi-NCR.", breadcrumb: "Schedule Pickup" }
  },
  {
    path: "/scrap-selling/how-it-works",
    name: "scrap-pickup",
    component: () => import("../views/ScrapGuide.vue"),
    props: { type: "pickup" },
    meta: { title: "How Scrap Pickup Works | Masterji Consultancy", description: "Understand the steps for arranging a scrap collection.", breadcrumb: "How Pickup Works" }
  },
  {
    path: "/scrap-selling/prices",
    name: "scrap-prices",
    component: () => import("../views/ScrapGuide.vue"),
    props: { type: "prices" },
    meta: { title: "Scrap Prices and Estimates | Masterji Consultancy", description: "Understand what affects scrap value and collection estimates.", breadcrumb: "Scrap Prices" }
  },
  {
    path: "/contact",
    name: "contact",
    component: () => import("../views/Contact.vue"),
    meta: {
      title: "Contact Us | Masterji Consultancy",
      description:
        "Get in touch with Masterji Consultancy for travel, solar, interior design, touring, or scrap collection enquiries.",
      breadcrumb: "Contact"
    }
  },
  {
    path: "/admin",
    name: "admin",
    component: () => import("../views/Admin.vue"),
    meta: { title: "Admin | Masterji Consultancy", description: "Private administration area.", breadcrumb: "Admin", noindex: true }
  },
  {
    path: "/terms-and-conditions",
    name: "terms",
    component: () => import("../views/Terms.vue"),
    meta: {
      title: "Terms & Conditions | Masterji Consultancy",
      description: "Terms and conditions for using Masterji Consultancy's website and services.",
      breadcrumb: "Terms & Conditions"
    }
  },
  {
    path: "/:pathMatch(.*)*",
    name: "not-found",
    component: () => import("../views/NotFound.vue"),
    meta: {
      title: "Page Not Found | Masterji Consultancy",
      description: "The page you're looking for doesn't exist or has moved.",
      breadcrumb: "Page Not Found",
      noindex: true
    }
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes,
  scrollBehavior() {
    return { top: 0 };
  }
});

export default router;
