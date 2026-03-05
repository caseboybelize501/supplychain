# AI Supply Chain Stress Tester

Simulate a thousand supply chain disasters before they happen.

## Overview

This platform enables companies to upload their supply chain graph and run Monte Carlo simulations across configurable disruption scenarios. It provides financial impact estimates, bottleneck heatmaps, and recovery time projections.

## Features

- Upload supply chain data (CSV or JSON)
- Run 1,000 simulation iterations in under 60 seconds
- Parallel Celery workers for scalability
- LLaMA-generated risk narratives with mitigation recommendations
- Interactive graph visualization
- PDF export of board-ready reports

## Stack

- **Frontend**: Next.js (supply chain graph viz + scenario builder + report)
- **Backend**: FastAPI (Python)
- **Simulation Engine**: NumPy + SciPy (Monte Carlo, parallel via Celery)
- **Database**: PostgreSQL (supply chains, scenarios, simulation results)
- **Queue**: Celery + Redis (parallel simulation workers)
- **Graph viz**: D3.js (interactive supply chain network map)
- **AI**: LLaMA.cpp via POST http://llama:8000/generate
- **Export**: ReportLab (PDF board report)

## Quick Start

1. Clone the repository
2. Run `docker-compose up`
3. Access the UI at http://localhost:3000

## API Endpoints

- `POST /api/supply-chain/upload` → Upload supply chain graph
- `POST /api/simulation/run` → Start simulation run
- `GET /api/simulation/:job_id` → Poll status + partial results
- `GET /api/simulation/:id/report` → Full results + narrative
- `POST /api/report/:id/export` → PDF download
- `GET /health` → Health check

## Scenario Library

1. Port Strike
2. Supplier Bankruptcy
3. Earthquake in Region
4. Demand Spike 3x
5. Tariff Increase 25%
6. Cyberattack ERP System
7. Pandemic Labor Shortage
8. Raw Material Shortage
9. Logistics Cost Spike
10. Single Source Failure
