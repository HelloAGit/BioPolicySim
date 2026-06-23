import json
from biopolicysim.engine import SimulationEngine

def load_personas():
    import os, json
    folder = os.path.join(os.path.dirname(__file__), "..", "personas")
    personas = {}
    for f in os.listdir(folder):
        if f.endswith(".json"):
            with open(os.path.join(folder, f)) as fp:
                data = json.load(fp)
                personas[data["name"]] = data
    return personas

if __name__ == "__main__":
    personas = load_personas()
    engine = SimulationEngine(personas)

    with open("policy_questions/sample_policy.txt") as f:
        policy = f.read()

    result = engine.run(policy)
    print(result)

