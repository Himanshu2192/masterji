-- Seed the four core services

INSERT INTO services (slug, name, description) VALUES
    ('tour_travel', 'Tour & Travel Bookings', 'Domestic and international trip planning, flights, hotels and packages.'),
    ('solar_panel', 'Solar Panel Installation', 'Residential and commercial solar setup, consultation and maintenance.'),
    ('interior_design', 'Interior Design', 'End-to-end interior design for homes and offices.'),
    ('touring_services', 'Touring Services', 'Guided local tours, itineraries and travel logistics.')
ON CONFLICT (slug) DO NOTHING;
