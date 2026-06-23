import re
from typing import List, Dict

class PolicyParser:
    TAG_RULES = {
        "genomics": r"\b(genomic|dna|sequencing)\b",
        "access_control": r"\b(access control|restricted|authorization)\b",
        "incident_reporting": r"\b(report|notify|escalate)\b",
        "model_eval": r"\b(eval|assessment|testing)\b",
    }

    def parse(self, text: str) -> List[str]:
        tags = []
        for tag, pattern in self.TAG_RULES.items():
            if re.search(pattern, text, re.IGNORECASE):
                tags.append(tag)
        return tags
class PolicyParser:
    """
    Minimal parser to extract simple tags from text.
    Extend this with your real parsing logic.
    """
    def parse(self, text):
        text_l = (text or "").lower()
        tags = set()
        if "genomic" in text_l or "genomics" in text_l:
            tags.add("genomics")
        if "access control" in text_l or ("access" in text_l and "control" in text_l):
            tags.add("access_control")
        return list(tags)
