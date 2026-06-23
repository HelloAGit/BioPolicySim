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
