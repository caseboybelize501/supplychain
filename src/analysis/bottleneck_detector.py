import numpy as np
from src.models import SupplyChain

class BottleneckDetector:
    def calculate_criticality(self, chain: SupplyChain):
        criticalities = {}
        for node in chain.nodes:
            dependents_count = len([e for e in chain.edges if e.target_id == node.id])
            no_alternative_flag = 1 if dependents_count == 0 else 0
            lead_time_score = min(node.lead_time_days / 90, 1)
            
            criticality = (dependents_count * 0.4) + (no_alternative_flag * 0.4) + (lead_time_score * 0.2)
            criticalities[node.id] = criticality
        return criticalities
