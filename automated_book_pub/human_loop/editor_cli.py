import os

def read_text(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

def write_text(file_path, text):
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(text)

def launch_editor():
    reviewed_path = "outputs/reviewed_chapter1.txt"
    human_edit_path = "outputs/human_edited_chapter1.txt"

    if not os.path.exists(reviewed_path):
        print("❌ Reviewed file not found.")
        return

    content = read_text(reviewed_path)

    print("\n📖 === AI Reviewed Chapter ===\n")
    print(content)
    print("\n✍️ === Now enter your edits below === (Type 'SAVE' on a new line to finish editing)\n")

    edited_lines = []
    while True:
        line = input()
        if line.strip().upper() == "SAVE":
            break
        edited_lines.append(line)

    final_text = "\n".join(edited_lines)
    write_text(human_edit_path, final_text)
    print(f"\n✅ Saved human-edited version to {human_edit_path}")

if __name__ == "__main__":
    launch_editor()
