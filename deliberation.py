from typing import Dict, List

class DeliberationEngine:
    def __init__(self, personas: Dict):
        self.personas = personas

    def initial_positions(self, tags: List[str]) -> Dict:
        output = {}
        for name, p in self.personas.items():
            score = sum(tag in p["interests"] for tag in tags)
            output[name] = "support" if score > 0 else "modify"
        return output

    def objections(self, tags: List[str]) -> Dict:
        obs = {}
        for name, p in self.personas.items():
            missing = [t for t in p["concerns"] if t not in tags]
            if missing:
                obs[name] = f"Missing safeguards: {', '.join(missing)}"
        return obs

    def final_votes(self, initial: Dict, objections: Dict) -> Dict:
        votes = {}
        for name in initial:
            votes[name] = "oppose" if name in objections else initial[name]
        return votes
