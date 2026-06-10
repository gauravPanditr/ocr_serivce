from fastapi import APIRouter, UploadFile, File
from src.service.gemini_service import extract_document
from src.service.prompts import FIR_PROMPT

router = APIRouter(
    prefix="/ocr",
    tags=["FIR OCR"]
)

@router.post("/fir")
async def fir_ocr(
    file: UploadFile = File(...)
):

    file_bytes = await file.read()

    result = extract_document(
        file_bytes,
        file.content_type,
        FIR_PROMPT
    )

    return {"data": result}