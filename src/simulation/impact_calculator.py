import numpy as np

class ImpactCalculator:
    def __init__(self):
        pass

    def calculate_financial_impact(self, stockout_days, revenue_at_risk):
        # Simplified financial impact calculation
        return {
            "total_loss": stockout_days * revenue_at_risk,
            "revenue_at_risk": revenue_at_risk
        }

    def calculate_recovery_time(self, disruption_params):
        # Recovery time based on disruption parameters
        if "duration_days" in disruption_params:
            return disruption_params["duration_days"] + np.random.exponential(2)
        elif "impact_duration" in disruption_params:
            return disruption_params["impact_duration"] + np.random.gamma(2, 1)
        else:
            return np.random.gamma(3, 2)

    def calculate_affected_skus(self, chain, disruption_params):
        # Determine affected SKUs based on disruption type
        return ["SKU001", "SKU002"]
