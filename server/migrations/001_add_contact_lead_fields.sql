-- Run once against an existing PostgreSQL database.
-- New installations are covered by db.create_all().
ALTER TABLE contact_inquiries
    ADD COLUMN IF NOT EXISTS company VARCHAR(160),
    ADD COLUMN IF NOT EXISTS preferred_contact VARCHAR(20),
    ADD COLUMN IF NOT EXISTS budget_range VARCHAR(50),
    ADD COLUMN IF NOT EXISTS timeline VARCHAR(50),
    ADD COLUMN IF NOT EXISTS status VARCHAR(20) NOT NULL DEFAULT 'new',
    ADD COLUMN IF NOT EXISTS internal_notes TEXT,
    ADD COLUMN IF NOT EXISTS updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP;

CREATE INDEX IF NOT EXISTS ix_contact_inquiries_status
    ON contact_inquiries (status);

CREATE INDEX IF NOT EXISTS ix_contact_inquiries_created_at
    ON contact_inquiries (created_at);
