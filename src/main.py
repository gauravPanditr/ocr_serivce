from fastapi import FastAPI, File, UploadFile
from google import genai
from google.genai import types
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

@app.post("/ocr/")
async def ocr(file: UploadFile = File(...)):
    file_bytes = await file.read()

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=[
            "Extract all text from this document. Return only the extracted text.",
            types.Part.from_bytes(
                data=file_bytes,
                mime_type=file.content_type
            )
        ]
    )

    return {"text": response.text}