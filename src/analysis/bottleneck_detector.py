import numpy as np
from collections import defaultdict

class BottleneckDetector:
    def __init__(self):
        pass

    def calculate_criticality(self, chain):
        # Calculate criticality score for each node
        criticalities = {}
        
        # For each node in the supply chain
        for node_id in chain.nodes:
            dependents_count = len(chain.get_dependents(node_id))
            no_alternative_flag = 1 if not chain.has_alternatives(node_id) else 0
            lead_time_days = chain.get_lead_time(node_id)
            
            # Weighted score calculation
            criticality = (dependents_count * 0.4) + (no_alternative_flag * 0.4) + ((lead_time_days / 90) * 0.2)
            criticalities[node_id] = min(1.0, max(0.0, criticality))  # Clamp between 0 and 1
        
        return criticalities

    def generate_heatmap(self, chain):
        criticalities = self.calculate_criticality(chain)
        return criticalities
