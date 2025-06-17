import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

# Configure the Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("models/gemini-1.5-flash")

def read_spun_text():
    with open("outputs/spun_chapter1.txt", "r", encoding="utf-8") as f:
        return f.read()

def save_reviewed_text(text):
    with open("outputs/reviewed_chapter1.txt", "w", encoding="utf-8") as f:
        f.write(text)

def save_review_feedback(feedback):
    with open("outputs/review_feedback.txt", "w", encoding="utf-8") as f:
        f.write(feedback)

def review_chapter_text(spun_text):
    # Ask for two separate outputs
    prompt = (
        "You are a professional book editor.\n"
        "First, provide a structured review of the following text using this format:\n"
        "- ✅ Grammar: ...\n"
        "- 💡 Clarity: ...\n"
        "- 🎯 Tone: ...\n"
        "- ✍️ Suggestions: ...\n\n"
        "Then, return an improved version of the text after the feedback.\n"
        "Start the edited version with '=== Edited Version ==='\n\n"
        f"Text to review:\n{spun_text}"
    )
    response = model.generate_content(prompt)
    return response.text

# Main logic
if __name__ == "__main__":
    spun_text = read_spun_text()
    full_review_output = review_chapter_text(spun_text)

    # Separate feedback and edited text using marker
    if "=== Edited Version ===" in full_review_output:
        parts = full_review_output.split("=== Edited Version ===")
        feedback_part = parts[0].strip()
        edited_part = parts[1].strip()
    else:
        feedback_part = "Could not extract feedback properly."
        edited_part = full_review_output.strip()

    # Save both
    save_review_feedback(feedback_part)
    save_reviewed_text(edited_part)

    print("[✔] Edited text saved to outputs/reviewed_chapter1.txt")
    print("[✔] Review feedback saved to outputs/review_feedback.txt")

__all__ = ["review_chapter_text"]
