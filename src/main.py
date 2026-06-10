from fastapi import FastAPI

from src.routes.insurance import router as insurance_router
from src.routes.repair_bill import router as repair_router

app = FastAPI(title="OCR Service")

app.include_router(insurance_router)
app.include_router(repair_router)
