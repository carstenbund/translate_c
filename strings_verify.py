import re
import os

def extract_valid_strings(source_file, output_file):
    with open(source_file, "r", encoding="utf-8") as file:
        content = file.read()

    # Regex to match sections marked as valid
    valid_section_pattern = re.compile(r'String: "(.*?)"\nLine (\d+):\n(.*?)Valid for translation: \[y\]', re.DOTALL)
    valid_sections = valid_section_pattern.findall(content)

    with open(output_file, "a", encoding="utf-8") as file:  # Append to the output file
        for string, line_num, context in valid_sections:
            file.write(f"{string}\n")

    print(f"Valid strings extracted and appended to {output_file}")

def process_directory(directory, output_file):
    for filename in os.listdir(directory):
        if filename.endswith(".strings"):
            source_file = os.path.join(directory, filename)
            extract_valid_strings(source_file, output_file)

if __name__ == "__main__":
    directory_path = "."
    output_file = os.path.join(directory_path, "strings_to_translate.txt")
    process_directory(directory_path, output_file)

