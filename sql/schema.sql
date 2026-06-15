CREATE TABLE IF NOT EXISTS bps_annual (
    id BIGSERIAL PRIMARY KEY,
    survey_date INTEGER NOT NULL,
    geography_type TEXT NOT NULL,
    state_fips TEXT NOT NULL,
    county_fips TEXT,
    place_fips TEXT,
    name TEXT NOT NULL,
    months_reported INTEGER,
    non_rep_unit_total INTEGER,
    source_url TEXT NOT NULL,
    raw_record_json JSONB NOT NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS permits (
    id BIGSERIAL PRIMARY KEY,
    source_system TEXT NOT NULL DEFAULT 'cityview',
    external_id TEXT,
    permit_number TEXT,
    jurisdiction TEXT,
    permit_type TEXT,
    status TEXT,
    address TEXT,
    applicant_name TEXT,
    contractor_name TEXT,
    units INTEGER,
    valuation NUMERIC,
    applied_at DATE,
    issued_at DATE,
    finaled_at DATE,
    raw_record_json JSONB NOT NULL DEFAULT '{}'::jsonb,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS contractors (
    id BIGSERIAL PRIMARY KEY,
    contractor_name TEXT NOT NULL,
    contact_name TEXT,
    email TEXT,
    phone TEXT,
    website TEXT,
    notes TEXT,
    source TEXT,
    raw_record_json JSONB NOT NULL DEFAULT '{}'::jsonb,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);
