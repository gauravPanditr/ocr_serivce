from fastapi import APIRouter, UploadFile, File
from src.service.gemini_service import extract_document
from src.service.prompts import REPAIR_BILL_PROMPT

router = APIRouter(
    prefix="/ocr",
    tags=["Repair Bill OCR"]
)

@router.post("/repair-bill")
async def repair_bill_ocr(
    file: UploadFile = File(...)
):

    file_bytes = await file.read()

    result = extract_document(
        file_bytes,
        file.content_type,
        REPAIR_BILL_PROMPT
    )

    return {"data": result}