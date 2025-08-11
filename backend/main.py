from fastapi import FastAPI, Form
import requests

app = FastAPI()

@app.post("/generate/")
def generate_business_ideas(industry: str = Form(...)):
    prompt = f"""
    You are an expert startup consultant.
    For the industry: {industry}
    Generate:
    1. Three startup ideas.
    2. A one-paragraph pitch for each.
    3. Suggested target audience.
    4. Suggested revenue model.
    Format clearly with headings.
    """
    
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={"model": "mistral", "prompt": prompt, "stream": False}
    )
    result = response.json()
    return {"ideas": result["response"].strip()}
