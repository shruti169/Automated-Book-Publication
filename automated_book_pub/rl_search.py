import chromadb
from chromadb.config import Settings
import random
import json

import chromadb
from chromadb.config import Settings

client = chromadb.PersistentClient(path="chroma_store")
collection = client.get_or_create_collection(name="chapter_versions")

# Simulated query
query_text = "Explain the role of AI in modern education"

# Retrieve top 5 similar versions
results = collection.query(query_texts=[query_text], n_results=5)

retrieved_texts = results["documents"][0]

# Simulated reward function (normally, feedback-driven)
def reward_function(text):
    """Mock reward based on length & keywords."""
    score = 0
    if "AI" in text: score += 0.3
    if "education" in text: score += 0.3
    if len(text) > 100: score += 0.2
    score += random.uniform(0, 0.2)  # simulate randomness or user preference
    return round(score, 2)

# Assign rewards to each retrieved text
rewards = [reward_function(text) for text in retrieved_texts]

# Select the best based on max reward
best_index = rewards.index(max(rewards))
best_text = retrieved_texts[best_index]

# Show result
print(f"🔍 Query: {query_text}")
print("\n📘 Best Retrieved Version:")
print(best_text)
print(f"\n🏆 Reward Score: {rewards[best_index]}")

# Optional: Save feedback to JSON for learning
feedback = {
    "query": query_text,
    "retrieved": retrieved_texts,
    "rewards": rewards,
    "selected_text": best_text,
    "selected_reward": rewards[best_index]
}

with open("outputs/rl_feedback.json", "w", encoding="utf-8") as f:
    json.dump(feedback, f, indent=2)

print("\n✅ Feedback saved to outputs/rl_feedback.json")
