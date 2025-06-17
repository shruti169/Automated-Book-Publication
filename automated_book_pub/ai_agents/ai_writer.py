import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Use a supported and available model
model = genai.GenerativeModel("models/gemini-1.5-flash")

def read_chapter_text():
    with open("outputs/chapter1_text.txt", "r", encoding="utf-8") as f:
        return f.read()

def save_spun_text(text):
    with open("outputs/spun_chapter1.txt", "w", encoding="utf-8") as f:
        f.write(text)

def spin_chapter_text(original_text):
    prompt = (
        "Rewrite the following chapter in a modern, engaging tone. Improve clarity and make it suitable for young adult readers:\n\n"
        f"{original_text}"
    )
    response = model.generate_content(prompt)
    return response.text

if __name__ == "__main__":
    text = read_chapter_text()
    spun_text = spin_chapter_text(text)
    save_spun_text(spun_text)
    print("[✔] Spun version saved to outputs/spun_chapter1.txt")
