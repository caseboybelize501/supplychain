from celery import Celery
from src.simulation.monte_carlo import MonteCarloSimulator
from src.models import SimRun, Result
from src.simulation.scenario_library import SCENARIOS
import json

app = Celery('supplychain_simulator')
app.config_from_object('django.conf:settings', namespace='CELERY')

@app.task(bind=True)
def run_simulation_task(self, chain_id, scenario_name, iterations):
    try:
        # Get scenario from library
        scenario = SCENARIOS[scenario_name]
        
        # Initialize simulator
        simulator = MonteCarloSimulator()
        
        # Run simulation (mocked for now)
        results = simulator.run_simulation(chain_id, scenario, iterations)
        
        # Save result to DB
        run = SimRun(
            chain_id=chain_id,
            scenario_id=scenario_name,
            iterations=iterations,
            status="completed"
        )
        
        result_obj = Result(
            run_id=run.id,
            stockout_days=json.dumps(results["stockout_days"]),
            revenue_at_risk=json.dumps(results["revenue_at_risk"]),
            recovery_time=json.dumps(results["recovery_time"]),
            affected_skus=json.dumps(results["affected_skus"])
        )
        
        return {
            "run_id": run.id,
            "status": "completed",
            "results": results
        }
    except Exception as e:
        self.update_state(state='FAILURE', meta={'exc': str(e)})
        raise
