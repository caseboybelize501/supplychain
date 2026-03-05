import requests
import json

class RiskNarrator:
    def __init__(self):
        self.llama_url = "http://llama:8000/generate"

    def generate_narrative(self, run, results):
        # Prepare prompt
        prompt = f"You are a supply chain risk consultant presenting to a board. Supply chain: {run.chain_id}. Scenario tested: {run.scenario_id}. Simulation results (1,000 runs): Revenue at risk p50: ${results['revenue_at_risk']['p50']} | p90: ${results['revenue_at_risk']['p90']} | p99: ${results['revenue_at_risk']['p99']} Recovery time p50: {results['recovery_time']['p50']} days | p90: {results['recovery_time']['p90']} days Top 3 bottleneck nodes: [NODES] Write a board-ready risk narrative. Return JSON: {{ executive_summary: string (100 words), key_findings: [string], mitigations: [{{ action, cost_estimate, risk_reduction_pct, roi_rank }}, ...], immediate_actions: [string], monitoring_kpis: [string] }}"
        
        # Call LLaMA API
        response = requests.post(self.llama_url, json={
            "prompt": prompt,
            "temperature": 0.3,
            "max_tokens": 1536
        })
        
        return response.json()
