from celery import Celery
from src.simulation.monte_carlo import MonteCarloEngine
from src.models import SupplyChain, Scenario, SimRun, Result
import json

celery_app = Celery('supplychain', broker='redis://localhost:6379/0')
engine = MonteCarloEngine()

@celery_app.task(bind=True)
def run_simulation_task(self, chain_id: str, scenario_id: str, iterations: int):
    try:
        # Fetch data from DB
        chain = SupplyChain.objects.get(id=chain_id)
        scenario = Scenario.objects.get(id=scenario_id)

        # Run simulation
        result = engine.run_simulation(chain, scenario, iterations)

        # Save result to DB
        sim_run = SimRun(chain_id=chain_id, scenario_id=scenario_id, iterations=iterations)
        sim_run.save()
        
        db_result = Result(sim_run_id=sim_run.id, **result)
        db_result.save()

        return {"status": "completed", "sim_run_id": sim_run.id}
    except Exception as e:
        self.update_state(state='FAILURE', meta={'exc': str(e)})
        raise
