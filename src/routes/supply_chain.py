from fastapi import APIRouter, UploadFile, File, HTTPException
from src.models import SupplyChain
import pandas as pd
import json

class SupplyChainUpload:
    chain_id: str
    name: str
    nodes: list
    edges: list

router = APIRouter(prefix="/supply-chain", tags=["Supply Chain"])

@router.post("/upload")
async def upload_supply_chain(file: UploadFile = File(...)):
    try:
        content = await file.read()
        if file.content_type == "application/json":
            data = json.loads(content.decode())
        elif file.content_type == "text/csv":
            df = pd.read_csv(content)
            data = df.to_dict(orient="records")
        else:
            raise HTTPException(status_code=400, detail="Unsupported file type")

        chain = SupplyChain(**data)
        # Save to DB here
        return {"chain_id": chain.id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
