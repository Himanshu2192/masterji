# Database migrations

Run migrations from the `server` directory with the PostgreSQL database selected
by `DATABASE_URL`:

```bash
psql "$DATABASE_URL" -v ON_ERROR_STOP=1 -f migrations/001_add_contact_lead_fields.sql
```

The migration is safe to run more than once because it uses
`ADD COLUMN IF NOT EXISTS` and `CREATE INDEX IF NOT EXISTS`.

New databases are created by `db.create_all()` when the application starts
locally. Existing databases must run each migration explicitly during
deployment.

Run the second migration after the first one to add scrap pickup booking
fields:

```bash
psql "$DATABASE_URL" -v ON_ERROR_STOP=1 -f migrations/002_add_scrap_pickup_fields.sql
```

Create the admin credentials table before using the admin API:

```bash
psql "$DATABASE_URL" -v ON_ERROR_STOP=1 -f migrations/003_add_admin_users.sql
ADMIN_USERNAME=admin ADMIN_PASSWORD='use-a-long-random-password' \
  DATABASE_URL="$DATABASE_URL" python scripts/create_admin.py
```

Admin authentication is available under `/api/admin`. Login accepts JSON
`username` and `password`, establishes a secure Flask session, and returns a
short-lived signed token that can also be sent as `Authorization: Bearer ...`.
Service and contact-inquiry CRUD endpoints under that prefix require auth.
