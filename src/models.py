from sqlalchemy import Column, Integer, String, Float, DateTime, Text
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
import uuid

Base = declarative_base()

class SupplyChain(Base):
    __tablename__ = "supply_chains"
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String)
    nodes = Column(Text)  # JSON string
    edges = Column(Text)  # JSON string
    created_at = Column(DateTime, default=datetime.utcnow)

class Scenario(Base):
    __tablename__ = "scenarios"
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String)
    description = Column(Text)
    parameters = Column(Text)  # JSON string
    created_at = Column(DateTime, default=datetime.utcnow)

class SimRun(Base):
    __tablename__ = "sim_runs"
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    chain_id = Column(String)
    scenario_id = Column(String)
    iterations = Column(Integer)
    status = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)


class Result(Base):
    __tablename__ = "results"
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    run_id = Column(String)
    stockout_days = Column(Text)  # JSON string
    revenue_at_risk = Column(Text)  # JSON string
    recovery_time = Column(Text)  # JSON string
    affected_skus = Column(Text)  # JSON string
    created_at = Column(DateTime, default=datetime.utcnow)
