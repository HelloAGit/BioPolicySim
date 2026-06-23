from biopolicysim.parser import PolicyParser

def test_parser_detects_tags():
    p = PolicyParser()
    tags = p.parse("Genomic data requires access control.")
    assert "genomics" in tags
    assert "access_control" in tags
