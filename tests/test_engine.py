from biopolicysim.engine import SimulationEngine

def test_engine_runs():
    personas = {
        "Test": {"interests": ["genomics"], "concerns": []}
    }
    engine = SimulationEngine(personas)
    result = engine.run("Genomic sequencing required.")
    assert "tags" in result
    assert "final_votes" in result
