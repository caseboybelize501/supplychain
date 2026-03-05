import numpy as np
from scipy import stats
from src.models import Result

class MonteCarloSimulator:
    def __init__(self):
        self.results = []

    def run_simulation(self, chain, scenario, iterations=1000):
        results = []
        for i in range(iterations):
            disruption_params = self.sample_disruption(scenario)
            impact = self.propagate_disruption(chain, disruption_params)
            results.append(impact)
        
        # Aggregate results
        aggregated = self.aggregate_results(results)
        return aggregated

    def sample_disruption(self, scenario):
        # Sample from distributions defined in scenario
        params = {}
        for param_name, dist_info in scenario.parameters.items():
            if dist_info["type"] == "normal":
                params[param_name] = stats.norm.rvs(loc=dist_info["mean"], scale=dist_info["std"])
            elif dist_info["type"] == "uniform":
                params[param_name] = stats.uniform.rvs(loc=dist_info["low"], scale=dist_info["high"] - dist_info["low"])
        return params

    def propagate_disruption(self, chain, disruption_params):
        # BFS propagation through supply chain graph
        # Simplified for example
        impact = {
            "stockout_days": np.random.exponential(2.0),
            "revenue_at_risk": np.random.normal(100000, 20000),
            "recovery_time": np.random.gamma(3, 2),
            "affected_skus": ["SKU001", "SKU002"]
        }
        return impact

    def aggregate_results(self, results):
        # Calculate p50, p90, p99 for each metric
        agg = {}
        for key in results[0].keys():
            values = [r[key] for r in results]
            agg[key] = {
                "p50": np.percentile(values, 50),
                "p90": np.percentile(values, 90),
                "p99": np.percentile(values, 99)
            }
        return agg
