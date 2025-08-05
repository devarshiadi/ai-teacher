from fastapi import FastAPI, UploadFile, File, Form, Request
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from google import genai
from google.genai import types
from PIL import Image
import io

# --- App Setup ---
app = FastAPI()

# Serve static and template files
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# --- GenAI Client Configuration ---
tmp_api_key = "AIzaSyCjMsYC-mDTwOr1at1-91EkMwI2O6eOvXg"  # <--- Replace with your secure key
client = genai.Client(api_key=tmp_api_key)

# --- Helper Function to Enrich System Instruction ---
def enrich_instruction(original: str) -> str:
    prefix = (
        "You're an ICIS (International Cadet International School AI teacher). "
        "Help concisely in 1-2 lines with a real-time example."
    )
    return f"{prefix}\n\n{original}"

# --- Frontend Route ---
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# --- Text Generation Endpoint ---
@app.post("/generate_text")
async def generate_text(
    system_instruction: str = Form(...),
    content: str = Form(...)
):
    config = types.GenerateContentConfig(system_instruction=enrich_instruction(system_instruction))
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        config=config,
        contents=content
    )
    return JSONResponse(content={"text": response.text})

# --- Image Analysis Endpoint ---
@app.post("/analyze_image")
async def analyze_image(
    file: UploadFile = File(...),
    prompt: str = Form(...)
):
    image_bytes = await file.read()
    image = Image.open(io.BytesIO(image_bytes))
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=[image, prompt]
    )
    return JSONResponse(content={"text": response.text})

# --- PDF Summarization Endpoint ---
@app.post("/summarize_pdf")
async def summarize_pdf(
    file: UploadFile = File(...),
    prompt: str = Form(...)
):
    data = await file.read()
    part = types.Part.from_bytes(
        data=data,
        mime_type='application/pdf'
    )
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=[part, prompt]
    )
    return JSONResponse(content={"text": response.text})

# --- Grounded Search Endpoint ---
@app.post("/grounded_search")
async def grounded_search(
    query: str = Form(...)
):
    grounding_tool = types.Tool(
        google_search=types.GoogleSearch()
    )
    config = types.GenerateContentConfig(tools=[grounding_tool])
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=query,
        config=config
    )
    return JSONResponse(content={"text": response.text})

# To run the app: uvicorn main:app --reload
