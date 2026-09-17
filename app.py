from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, Response
from fastapi.templating import Jinja2Templates
import uvicorn
import os
from pathlib import Path
from textSummarizer.pipeline.prediction import PredictionPipeline

app = FastAPI(title="Text Summarizer API")

BASE_DIR = Path(__file__).resolve().parent
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")

@app.post("/predict")
async def predict_route(text: str = Form(...)):
    try:
        obj = PredictionPipeline()
        summary = obj.predict(text)
        return {"summary": summary}
    except Exception as e:
        return Response(f"Error Occurred: {e}", status_code=500)

@app.get("/train")
async def training():
    try:
        os.system("python main.py")
        return Response("Training successful!")
    except Exception as e:
        return Response(f"Error Occurred: {e}", status_code=500)

if __name__ == "__main__":
    print("\n" + "="*50)
    print("🚀 Server running!")
    print("👉 Open in browser: http://localhost:8080  OR  http://127.0.0.1:8080")
    print("="*50 + "\n")
    uvicorn.run(app, host="0.0.0.0", port=8080)
