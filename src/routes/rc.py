from fastapi import APIRouter, UploadFile, File
from src.service.gemini_service import extract_document
from src.service.prompts import RC_PROMPT

router = APIRouter(
    prefix="/ocr",
    tags=["RC OCR"]
)

@router.post("/rc")
async def rc_ocr(
    file: UploadFile = File(...)
):

    file_bytes = await file.read()

    result = extract_document(
        file_bytes,
        file.content_type,
        RC_PROMPT
    )

    return {"data": result}