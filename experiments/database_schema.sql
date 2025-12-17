-- Database schema for atomic data storage

CREATE TABLE IF NOT EXISTS elements (
    atomic_number INTEGER PRIMARY KEY,
    symbol TEXT NOT NULL UNIQUE,
    name TEXT NOT NULL,
    atomic_mass REAL,
    atomic_mass_kg REAL,
    atomic_radius_pm REAL,
    atomic_volume_m3 REAL,
    k_coefficient REAL,
    k_log10 REAL,
    period INTEGER,
    element_group INTEGER,
    zeff REAL,
    block TEXT,

    -- Additional properties
    density REAL,
    en_allen REAL,
    en_pauling REAL,
    electron_affinity REAL,
    vdw_radius REAL,
    covalent_radius_cordero REAL,
    metallic_radius REAL,
    atomic_volume REAL,

    -- Structural properties
    lattice_structure TEXT,
    lattice_constant REAL,

    -- Thermodynamic properties
    melting_point REAL,
    boiling_point REAL,
    specific_heat_capacity REAL,
    thermal_conductivity REAL,

    -- Electromagnetic properties
    electrical_resistivity REAL,
    magnetic_ordering TEXT,

    -- Computed derived parameters
    zeff_over_v REAL,
    zeff2_over_v REAL,
    k_over_zeff REAL,
    surface_area REAL,
    cross_section REAL,
    mass_density_atomic REAL,

    -- Metadata
    calculated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS cache_metadata (
    key TEXT PRIMARY KEY,
    value TEXT,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insert initial metadata
INSERT OR REPLACE INTO cache_metadata (key, value) VALUES ('schema_version', '1.0');
INSERT OR REPLACE INTO cache_metadata (key, value) VALUES ('description', 'Atomic data for research_inertia analysis');

-- Index for common queries
CREATE INDEX IF NOT EXISTS idx_k_coefficient ON elements(k_coefficient);
CREATE INDEX IF NOT EXISTS idx_zeff ON elements(zeff);
CREATE INDEX IF NOT EXISTS idx_block ON elements(block);
CREATE INDEX IF NOT EXISTS idx_period ON elements(period);
