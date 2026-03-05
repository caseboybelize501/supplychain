import requests
import json

class RiskNarrator:
    def __init__(self):
        self.llama_url = "http://llama:8000/generate"

    def generate_narrative(self, sim_run, result):
        prompt = f"You are a supply chain risk consultant presenting to a board. Supply chain: [CHAIN_SUMMARY]. Scenario tested: [SCENARIO]. Simulation results (1,000 runs): Revenue at risk p50: ${result['p50']['revenue_at_risk']} | p90: ${result['p90']['revenue_at_risk']} | p99: ${result['p99']['revenue_at_risk']} Recovery time p50: {result['p50']['recovery_time']} days | p90: {result['p90']['recovery_time']} days Top 3 bottleneck nodes: [NODES] Write a board-ready risk narrative. Return JSON: {{ executive_summary: string (100 words), key_findings: [string], mitigations: [{{ action, cost_estimate, risk_reduction_pct, roi_rank }}], immediate_actions: [string], monitoring_kpis: [string] }}"

        response = requests.post(self.llama_url, json={
            "prompt": prompt,
            "temperature": 0.3,
            "max_tokens": 1536
        })

        return response.json()
