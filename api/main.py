from fastapi import FastAPI
from pydantic import BaseModel
import json
import os

from biopolicysim.engine import SimulationEngine

app = FastAPI(title="BioPolicySim API")

# -----------------------------
# Load personas once at startup
# -----------------------------
def load_personas():
    folder = os.path.join(os.path.dirname(__file__), "..", "personas")
    personas = {}
    for f in os.listdir(folder):
        if f.endswith(".json"):
            with open(os.path.join(folder, f)) as fp:
                data = json.load(fp)
                personas[data["name"]] = data
    return personas

PERSONAS = load_personas()
ENGINE = SimulationEngine(PERSONAS)

# -----------------------------
# Request model
# -----------------------------
class PolicyRequest(BaseModel):
    policy_text: str

# -----------------------------
# Routes
# -----------------------------
@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/simulate")
def simulate(req: PolicyRequest):
    result = ENGINE.run(req.policy_text)
    return result

@app.get("/")
def root():
    return {
        "message": "BioPolicySim API",
        "endpoints": {
            "simulate": "/simulate",
            "streamlit": "/streamlit"
        }
    }
