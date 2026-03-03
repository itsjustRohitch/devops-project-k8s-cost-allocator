import os
import psycopg2
from kubernetes import client, config
import yaml
import time

def load_config():
    with open('src/config/config.yaml', 'r') as file:
        return yaml.safe_load(file)

def get_namespace_costs():
    return {"backend-team": {"cpu_cost": 1.50, "mem_cost": 0.80}}

def save_to_db(costs):
    max_retries = 5
    for attempt in range(max_retries):
        try:
            conn = psycopg2.connect(
                host=os.getenv("DB_HOST", "localhost"),
                database=os.getenv("POSTGRES_DB", "devopsdb"),
                user=os.getenv("POSTGRES_USER", "devopsuser"),
                password=os.getenv("POSTGRES_PASSWORD", "devopspass")
            )
            cur = conn.cursor()
            for ns, cost in costs.items():
                cur.execute(
                    "INSERT INTO namespace_costs (namespace, cpu_cost, memory_cost) VALUES (%s, %s, %s)",
                    (ns, cost['cpu_cost'], cost['mem_cost'])
                )
            conn.commit()
            cur.close()
            conn.close()
            print("Database insertion successful.")
            return
        except psycopg2.OperationalError:
            print(f"Database unavailable. Retrying in 5 seconds... ({attempt+1}/{max_retries})")
            time.sleep(5)
    print("Critical Failure: Database connection aborted.")

if __name__ == "__main__":
    while True:
        costs = get_namespace_costs()
        save_to_db(costs)
        print("Waiting for next hourly cycle...")
        time.sleep(3600)