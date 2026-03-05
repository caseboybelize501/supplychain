import numpy as np
from src.models import SupplyChain

class ImpactCalculator:
    def calculate_impact(self, chain: SupplyChain, params: dict):
        # Simplified impact calculation
        revenue_at_risk = 0
        stockout_days = []
        recovery_time = 0
        affected_skus = []

        for node in chain.nodes:
            if "capacity_loss" in params and np.random.rand() < 0.1:  # 10% chance of disruption
                capacity_loss = params["capacity_loss"]
                stockout_days.append(capacity_loss * node.capacity)
                revenue_at_risk += node.inventory_level * 0.5  # Simplified
                recovery_time += np.random.normal(10, 2)  # Days to recover
                affected_skus.append(node.id)

        return {
            "revenue_at_risk": revenue_at_risk,
            "stockout_days": stockout_days,
            "recovery_time": recovery_time,
            "affected_skus": affected_skus
        }
