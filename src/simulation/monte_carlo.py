import numpy as np
from scipy.stats import norm, uniform
from src.models import SupplyChain, SimRun, Result
from src.simulation.impact_calculator import ImpactCalculator
from src.analysis.bottleneck_detector import BottleneckDetector

class MonteCarloEngine:
    def __init__(self):
        self.calculator = ImpactCalculator()
        self.detector = BottleneckDetector()

    def run_simulation(self, chain: SupplyChain, scenario: Scenario, iterations: int = 1000):
        results = []
        for i in range(iterations):
            disruption_params = self.sample_disruption(scenario)
            impact = self.propagate_disruption(chain, disruption_params)
            results.append(impact)

        aggregated = self.aggregate_results(results)
        return aggregated

    def sample_disruption(self, scenario: Scenario):
        params = {}
        for key, value in scenario.parameters.items():
            if value["type"] == "normal":
                params[key] = norm.rvs(loc=value["mean"], scale=value["std"])
            elif value["type"] == "uniform":
                params[key] = uniform.rvs(loc=value["low"], scale=value["high"] - value["low"])
        return params

    def propagate_disruption(self, chain: SupplyChain, params: dict):
        # Simplified BFS propagation
        impact = self.calculator.calculate_impact(chain, params)
        return impact

    def aggregate_results(self, results):
        p50 = {k: np.percentile([r[k] for r in results], 50) for k in results[0].keys()}
        p90 = {k: np.percentile([r[k] for r in results], 90) for k in results[0].keys()}
        p99 = {k: np.percentile([r[k] for r in results], 99) for k in results[0].keys()}
        return {"p50": p50, "p90": p90, "p99": p99}
