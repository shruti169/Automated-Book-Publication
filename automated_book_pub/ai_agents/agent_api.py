# ai_agents/agent_api.py

from ai_agents.ai_writer import spin_chapter_text
from ai_agents.ai_reviewer import review_chapter_text


def run_agentic_pipeline(input_text):
    print("[AgenticAPI] Starting Writer Agent...")
    spun = spin_chapter_text(input_text)
    
    print("[AgenticAPI] Writer Agent complete.")
    print("[AgenticAPI] Starting Reviewer Agent...")
    reviewed = review_chapter_text(spun)
    
    print("[AgenticAPI] Reviewer Agent complete.")
    return reviewed
