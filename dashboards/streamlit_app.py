import streamlit as st
import json
from biopolicysim.engine import SimulationEngine

st.title("BioPolicySim Prototype")

policy_text = st.text_area("Paste policy text")

if st.button("Run Simulation"):
    personas = {}
    import os
    folder = os.path.join(os.path.dirname(__file__), "..", "personas")
    for f in os.listdir(folder):
        if f.endswith(".json"):
            with open(os.path.join(folder, f)) as fp:
                data = json.load(fp)
                personas[data["name"]] = data

    engine = SimulationEngine(personas)
    result = engine.run(policy_text)

    st.subheader("Detected Tags")
    st.write(result["tags"])

    st.subheader("Initial Positions")
    st.write(result["initial_positions"])

    st.subheader("Objections")
    st.write(result["objections"])

    st.subheader("Final Votes")
    st.write(result["final_votes"])

    st.subheader("Fragility Score")
    st.write(result["fragility_score"])
