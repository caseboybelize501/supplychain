# AI Supply Chain Stress Tester

Simulate a thousand supply chain disasters before they happen.

## Features
- Upload supply chain graph (CSV/JSON)
- Run Monte Carlo simulations across 10 preset disruption scenarios
- Parallel Celery workers for 1,000 simulations in under 60 seconds
- LLaMA-generated board-ready risk narratives with mitigation recommendations
- Interactive D3.js visualization of supply chain network
- PDF export of risk reports

## Stack
- Backend: FastAPI (Python)
- Simulation: NumPy + SciPy (Monte Carlo, parallel via Celery)
- Database: PostgreSQL
- Queue: Celery + Redis
- Frontend: Next.js (D3.js for graph viz)
- AI: LLaMA.cpp via POST http://llama:8000/generate
- Export: ReportLab (PDF board report)

## Quick Start
1. `docker-compose up`
2. Visit `http://localhost:3000` to start building your supply chain graph
3. Run simulations and generate risk reports

## Endpoints
- `POST /api/supply-chain/upload` → Upload supply chain graph
- `POST /api/simulation/run` → Start simulation run
- `GET /api/simulation/:job_id` → Poll status
- `GET /api/simulation/:id/report` → Get full results + narrative
- `POST /api/report/:id/export` → Export to PDF
- `GET /health` → Health check
