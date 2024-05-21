from fastapi import FastAPI,  File, UploadFile,  HTTPException
from fastapi.responses import JSONResponse, RedirectResponse

import torch
import whisper

# Checking if NVIDIA GPU is available
torch.cuda.is_available()
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

# Load the Whisper model:
model = whisper.load_model("base", device=DEVICE)

app = FastAPI()

@app.post("/whisper")
async def handler(file: UploadFile = File(...)):
    if not file:
        return JSONResponse(content={'status_code': 400, 'detail': 'No files were provided'})

    try:
        transcription = model.transcribe(file)
        return JSONResponse(content={'transcription': transcription["text"]})
    
    except Exception as e:
        return JSONResponse(content={'status_code': 400, 'detail': e})

@app.get("/", response_class=RedirectResponse)
async def redirect_to_docs():
    return "/docs"