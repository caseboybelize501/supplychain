from pydantic import BaseModel
from typing import List, Optional
import uuid

class Node(BaseModel):
    id: str
    name: str
    type: str  # factory, supplier, distribution_center
    lead_time_days: int
    inventory_level: int
    capacity: int


class Edge(BaseModel):
    source_id: str
    target_id: str
    distance_km: float
    cost_per_unit: float


class SupplyChain(BaseModel):
    id: str = str(uuid.uuid4())
    name: str
    nodes: List[Node]
    edges: List[Edge]


class Scenario(BaseModel):
    id: str = str(uuid.uuid4())
    name: str
    description: str
    parameters: dict


class SimRun(BaseModel):
    id: str = str(uuid.uuid4())
    chain_id: str
    scenario_id: str
    iterations: int
    status: str  # pending, running, completed


class Result(BaseModel):
    id: str = str(uuid.uuid4())
    sim_run_id: str
    p50: dict
    p90: dict
    p99: dict
