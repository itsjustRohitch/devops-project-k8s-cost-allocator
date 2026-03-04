# Kubernetes Cost Allocator

A **DevOps-oriented system** that extracts Kubernetes namespace resource utilization, calculates associated infrastructure costs using predefined pricing models, and persists the results into a PostgreSQL database.  

The project demonstrates practical implementation of:

- Containerization
- Orchestration
- Continuous Integration / Continuous Delivery
- Infrastructure as Code

---

# Project Overview

The **Kubernetes Cost Allocator** analyzes resource usage across Kubernetes namespaces and maps that usage to infrastructure cost estimates.  

The system periodically:

1. Collects namespace resource usage from Kubernetes
2. Applies pricing models defined in configuration files
3. Calculates estimated infrastructure costs
4. Stores results in a PostgreSQL database
5. Runs continuously in a containerized environment

This architecture simulates **cost attribution systems used in enterprise Kubernetes environments**.

---

# Technology Stack

| Layer | Technology |
|------|-------------|
| Application Logic | Python 3.9 |
| Data Persistence | PostgreSQL |
| Containerization | Docker, Docker Compose |
| Orchestration | Kubernetes (Local / Kubeadm / Docker Desktop) |
| CI/CD | GitHub Actions |
| Security Scanning | Trivy |
| Testing | Pytest |

---

# Repository Structure

```

.
├── .github/
│   └── workflows/
│       └── ci-cd.yml              # CI/CD pipeline configuration
│
├── deliverables/
│   └── demo-video/                # Final submission artifacts
│
├── docs/
│   ├── architecture.md            # System design
│   ├── user-guide.md              # Usage documentation
│   └── planning.md                # Project planning
│
├── infrastructure/
│   ├── docker/
│   │   └── Dockerfile             # Application container definition
│   │
│   └── kubernetes/
│       ├── deployment.yaml        # App deployment
│       ├── service.yaml           # Service definition
│       └── configmap.yaml         # Configuration injection
│
├── monitoring/
│   ├── alerts.yaml                # Alert rules
│   └── dashboards.json            # Monitoring dashboards
│
├── scripts/
│   └── init.sql                   # Database initialization
│
├── src/
│   ├── config/
│   │   └── pricing.yaml           # Pricing model definitions
│   │
│   └── main/python/
│       └── allocator.py           # Core cost allocation logic
│
├── tests/
│   └── unit/
│       └── test_allocator.py      # Unit tests
│
├── docker-compose.yml             # Local orchestration configuration
├── requirements.txt               # Python dependencies
└── README.md                      # Project documentation

````

---

# Execution Guide

## Prerequisites

Ensure the following tools are installed and configured:

- **Docker Desktop**
- **Kubernetes enabled in Docker Desktop**
- **kubectl CLI**
- **Docker Compose**

---

# Phase 1 — Local Container Execution

Run the application locally using **Docker Compose**.

### Build and start containers

```bash
docker compose up --build -d
````

This command:

* Builds the application container
* Starts the PostgreSQL container
* Starts the Python allocator service

---

### Verify application logs

```bash
docker compose logs -f app
```

Expected output:

```
Database insertion successful. Waiting for next hourly cycle...
```

This indicates:

* Kubernetes resource usage collected
* Cost calculated
* Data stored in PostgreSQL

---

### Stop local containers

```bash
docker compose down
```

This stops and removes all containers and associated networks.

---

# Phase 2 — Kubernetes Orchestration

Deploy the system to a **local Kubernetes cluster**.

---

## Deploy Kubernetes resources

```bash
kubectl apply -f infrastructure/kubernetes/
```

This creates:

* Deployment
* Service
* ConfigMaps
* Application Pods

---

## Verify cluster resources

```bash
kubectl get pods,svc,deploy
```

Example output:

```
NAME                        READY   STATUS    RESTARTS
cost-allocator-pod          1/1     Running   0

NAME                 TYPE        CLUSTER-IP
cost-allocator-svc   ClusterIP   10.96.10.23

NAME                        READY
cost-allocator-deployment   1/1
```

---

## Remove Kubernetes resources

```bash
kubectl delete -f infrastructure/kubernetes/
```

This removes all deployed services, pods, and deployments.

---

# CI/CD Pipeline

The project includes a **GitHub Actions pipeline** that performs:

1. **Automated testing** using Pytest
2. **Container image build**
3. **Security vulnerability scanning** using Trivy

The workflow is defined in:

```
.github/workflows/ci-cd.yml
```

Pipeline stages:

1. Code push to `main`
2. Run unit tests
3. Build Docker image
4. Scan image for vulnerabilities

---

# Monitoring

The project includes monitoring assets:

* Alerting rules
* Dashboard configurations

Located in:

```
monitoring/
```

These files can integrate with tools such as:

* Prometheus
* Grafana

---

# Deliverables

The `deliverables/` directory contains materials for project evaluation:

* Demonstration video
* Project documentation
* Deployment proof

---

# Summary

The **Kubernetes Cost Allocator** demonstrates core DevOps practices:

* Container-based application deployment
* Infrastructure as Code
* CI/CD automation
* Kubernetes orchestration
* Cost attribution for resource usage

The system simulates how organizations **track Kubernetes resource consumption and map it to operational costs** across teams and namespaces.
