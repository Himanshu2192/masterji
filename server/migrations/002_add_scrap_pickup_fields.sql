ALTER TABLE contact_inquiries
    ADD COLUMN IF NOT EXISTS pickup_address TEXT,
    ADD COLUMN IF NOT EXISTS pickup_date DATE,
    ADD COLUMN IF NOT EXISTS pickup_time VARCHAR(30);
