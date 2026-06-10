from fastapi import APIRouter, UploadFile, File
from src.service.gemini_service import extract_document
from src.service.prompts import INSURANCE_PROMPT

router = APIRouter(
    prefix="/ocr",
    tags=["Insurance OCR"]
)

@router.post("/insurance")
async def insurance_ocr(
    file: UploadFile = File(...)
):

    file_bytes = await file.read()

    result = extract_document(
        file_bytes,
        file.content_type,
        INSURANCE_PROMPT
    )

    return {"data": result}