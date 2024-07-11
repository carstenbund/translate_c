import os
import re

def load_translations(nl_file, en_file):
    with open(nl_file, "r", encoding="utf-8") as file:
        nl_comments = [comment.strip() for comment in file.read().split("\n\n")]

    with open(en_file, "r", encoding="utf-8") as file:
        en_comments = [comment.strip() for comment in file.read().split("\n\n")]

    translations = dict(zip(nl_comments, en_comments))

    return translations

def apply_translations(source_file, translations):
    with open(source_file, "r", encoding="utf-8") as file:
        content = file.read()

    for nl_comment, en_comment in translations.items():
        # Use re.escape to handle special characters in comments
        content = re.sub(re.escape(nl_comment), en_comment, content, flags=re.DOTALL)

    output_file = source_file.replace(".c", "_translated.c")
    with open(output_file, "w", encoding="utf-8") as file:
        file.write(content)

    print(f"Translations applied. Check the updated source file: {output_file}")

def process_directory(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".c"):
            source_file = os.path.join(directory, filename)
            nl_file = os.path.join(directory, filename + ".en.txt")
            en_file = os.path.join(directory, filename + ".jp.txt")

            if os.path.exists(nl_file) and os.path.exists(en_file):
                translations = load_translations(nl_file, en_file)
                apply_translations(source_file, translations)
            else:
                print(f"Translation files for {filename} not found.")

if __name__ == "__main__":
    directory_path = "."
    process_directory(directory_path)

