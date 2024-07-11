import re
import os

def extract_strings_with_context(source_file, output_file):
    with open(source_file, "r", encoding="utf-8") as file:
        lines = file.readlines()

    pattern = re.compile(r'"(.*?)"')
    extracted_data = []

    for line_num, line in enumerate(lines):
        matches = pattern.findall(line)
        for match in matches:
            context_start = max(0, line_num - 2)
            context_end = min(len(lines), line_num + 3)
            context = "".join(lines[context_start:context_end])
            extracted_data.append((match, line_num + 1, context))

    with open(output_file, "w", encoding="utf-8") as file:
        for string, line_num, context in extracted_data:
            file.write(f"String: \"{string}\"\n")
            file.write(f"Line {line_num}:\n{context}")
            file.write(f"Valid for translation: [ ]\n")
            file.write("-" * 80 + "\n\n")

    print(f"Strings with context extracted to {output_file}")

def process_directory(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".c"):
            source_file = os.path.join(directory, filename)
            output_file = os.path.join(directory, filename + ".strings")
            extract_strings_with_context(source_file, output_file)

if __name__ == "__main__":
    directory_path = "."
    process_directory(directory_path)

