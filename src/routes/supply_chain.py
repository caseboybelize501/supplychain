from fastapi import APIRouter, UploadFile, File, HTTPException
from src.models import SupplyChain
import json
import csv

class SupplyChainUpload:
    def __init__(self):
        self.chain_id = None

supply_chain_router = APIRouter()

@supply_chain_router.post("/upload")
def upload_supply_chain(file: UploadFile = File(...)):
    try:
        content = file.file.read().decode('utf-8')
        if file.content_type == "application/json":
            data = json.loads(content)
        elif file.content_type == "text/csv":
            reader = csv.DictReader(content.splitlines())
            data = list(reader)
        else:
            raise HTTPException(status_code=400, detail="Unsupported file type")
        
        # Save to DB
        chain = SupplyChain(**data)
        return {"chain_id": chain.id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
