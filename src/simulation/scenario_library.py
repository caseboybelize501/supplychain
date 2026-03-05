from src.models import Scenario

SCENARIOS = {
    "port_strike": Scenario(
        name="Port Strike",
        description="Disruption due to port labor strike",
        parameters={
            "duration_days": {"type": "normal", "mean": 14, "std": 5},
            "capacity_loss_pct": {"type": "uniform", "low": 0.3, "high": 0.9}
        }
    ),
    "supplier_bankruptcy": Scenario(
        name="Supplier Bankruptcy",
        description="Key supplier goes bankrupt",
        parameters={
            "recovery_time_days": {"type": "normal", "mean": 30, "std": 10}
        }
    ),
    "earthquake_region": Scenario(
        name="Earthquake in Region",
        description="Natural disaster affecting regional suppliers",
        parameters={
            "impact_radius_km": {"type": "normal", "mean": 50, "std": 15},
            "capacity_loss_pct": {"type": "uniform", "low": 0.2, "high": 0.8}
        }
    ),
    "demand_spike_3x": Scenario(
        name="Demand Spike 3x",
        description="Unexpected 3x increase in demand",
        parameters={
            "multiplier": {"type": "normal", "mean": 3.0, "std": 0.5}
        }
    ),
    "tariff_increase_25pct": Scenario(
        name="Tariff Increase 25%",
        description="New tariffs increase import costs by 25%",
        parameters={
            "cost_increase_pct": {"type": "normal", "mean": 25, "std": 5}
        }
    ),
    "cyberattack_erp": Scenario(
        name="Cyberattack ERP System",
        description="ERP system compromised by cyberattack",
        parameters={
            "downtime_hours": {"type": "normal", "mean": 72, "std": 24}
        }
    ),
    "pandemic_labor_shortage": Scenario(
        name="Pandemic Labor Shortage",
        description="Labor shortage due to pandemic",
        parameters={
            "capacity_loss_pct": {"type": "uniform", "low": 0.1, "high": 0.5}
        }
    ),
    "raw_material_shortage": Scenario(
        name="Raw Material Shortage",
        description="Shortage of key raw materials",
        parameters={
            "shortage_duration_days": {"type": "normal", "mean": 10, "std": 3}
        }
    ),
    "logistics_cost_spike": Scenario(
        name="Logistics Cost Spike",
        description="Unexpected spike in logistics costs",
        parameters={
            "cost_multiplier": {"type": "normal", "mean": 1.5, "std": 0.3}
        }
    ),
    "single_source_failure": Scenario(
        name="Single Source Failure",
        description="Failure of single supplier source",
        parameters={
            "recovery_time_days": {"type": "normal", "mean": 20, "std": 5}
        }
    )
}
