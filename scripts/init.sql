CREATE TABLE IF NOT EXISTS namespace_costs (
    id SERIAL PRIMARY KEY,
    namespace VARCHAR(255) NOT NULL,
    cpu_cost NUMERIC(10, 4) NOT NULL,
    memory_cost NUMERIC(10, 4) NOT NULL,
    recorded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);