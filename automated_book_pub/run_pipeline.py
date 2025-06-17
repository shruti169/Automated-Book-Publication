# run_pipeline.py

from ai_agents.agent_api import run_agentic_pipeline

import os

raw_path = "outputs/raw_chapter.txt"
if not os.path.exists(raw_path):
    print(f"[❌] Missing input file: {raw_path}")
    exit(1)

with open(raw_path, "r", encoding="utf-8") as f:
    raw_text = f.read()

    chapter = f.read()

final_output = run_agentic_pipeline(chapter)

# Save the reviewed output
with open("outputs/reviewed_chapter.txt", "w", encoding="utf-8") as f:
    f.write(final_output)

print("✅ Pipeline completed and output saved.")
