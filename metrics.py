def compute_fragility_score(votes: dict) -> float:
    oppose = sum(v == "oppose" for v in votes.values())
    total = len(votes)
    return oppose / total if total else 0.0
