import numpy as np
from scipy import stats

SCENARIOS = {
    "port_strike": {
        "name": "Port Strike",
        "description": "Disruption due to port labor strike",
        "parameters": {
            "duration_days": {"type": "normal", "mean": 14, "std": 5},
            "capacity_loss": {"type": "uniform", "low": 0.3, "high": 0.9}
        }
    },
    "supplier_bankruptcy": {
        "name": "Supplier Bankruptcy",
        "description": "Critical supplier goes bankrupt",
        "parameters": {
            "impact_duration": {"type": "normal", "mean": 30, "std": 10},
            "recovery_time": {"type": "gamma", "shape": 2, "scale": 5}
        }
    },
    "earthquake_region": {
        "name": "Earthquake in Region",
        "description": "Natural disaster affecting regional suppliers",
        "parameters": {
            "magnitude": {"type": "normal", "mean": 7.0, "std": 1.0},
            "affected_percentage": {"type": "uniform", "low": 0.2, "high": 0.8}
        }
    },
    "demand_spike_3x": {
        "name": "Demand Spike 3x",
        "description": "Unexpected 3x demand increase",
        "parameters": {
            "multiplier": {"type": "normal", "mean": 3.0, "std": 0.5}
        }
    },
    "tariff_increase_25pct": {
        "name": "Tariff Increase 25%",
        "description": "New tariffs increase import costs by 25%",
        "parameters": {
            "increase_pct": {"type": "normal", "mean": 25, "std": 5}
        }
    },
    "cyberattack_erp": {
        "name": "Cyberattack ERP System",
        "description": "ERP system compromised by cyberattack",
        "parameters": {
            "downtime_hours": {"type": "normal", "mean": 48, "std": 12},
            "data_loss_pct": {"type": "uniform", "low": 0.1, "high": 0.5}
        }
    },
    "pandemic_labor_shortage": {
        "name": "Pandemic Labor Shortage",
        "description": "Labor shortage due to pandemic",
        "parameters": {
            "shortage_pct": {"type": "uniform", "low": 0.1, "high": 0.4}
        }
    },
    "raw_material_shortage": {
        "name": "Raw Material Shortage",
        "description": "Shortage of key raw materials",
        "parameters": {
            "shortage_duration": {"type": "gamma", "shape": 3, "scale": 2},
            "supply_reduction_pct": {"type": "uniform", "low": 0.1, "high": 0.6}
        }
    },
    "logistics_cost_spike": {
        "name": "Logistics Cost Spike",
        "description": "Unexpected spike in logistics costs",
        "parameters": {
            "cost_increase_pct": {"type": "normal", "mean": 30, "std": 10}
        }
    },
    "single_source_failure": {
        "name": "Single Source Failure",
        "description": "Failure of single supplier in critical path",
        "parameters": {
            "failure_probability": {"type": "uniform", "low": 0.01, "high": 0.1}
        }
    }
}
