from .parser import PolicyParser
from .deliberation import DeliberationEngine
from .metrics import compute_fragility_score

class SimulationEngine:
    def __init__(self, personas: dict):
        self.parser = PolicyParser()
        self.delib = DeliberationEngine(personas)

    def run(self, policy_text: str):
        tags = self.parser.parse(policy_text)
        initial = self.delib.initial_positions(tags)
        objections = self.delib.objections(tags)
        final_votes = self.delib.final_votes(initial, objections)
        fragility = compute_fragility_score(final_votes)

        return {
            "tags": tags,
            "initial_positions": initial,
            "objections": objections,
            "final_votes": final_votes,
            "fragility_score": fragility,
        }
