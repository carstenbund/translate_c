#!/usr/bin/python3

import re
import os

def extract_comments(source_file, output_file):
    with open(source_file, "r", encoding="utf-8") as file:
        content = file.read()

    # Regex to match C-style comments including multi-line and single-line comments
    multiline_comments = re.findall(r'/\*.*?\*/', content, re.DOTALL)
    singleline_comments = re.findall(r'//.*', content)

    with open(output_file, "w", encoding="utf-8") as file:
        seen_comments = set()
        for comment in multiline_comments + singleline_comments:
            comment = comment.strip()
            if comment not in seen_comments:
                seen_comments.add(comment)
                file.write(comment + "\n\n")

    print(f"Comments extracted to {output_file}")

def process_directory(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".c"):
            source_file = os.path.join(directory, filename)
            output_file = os.path.join(directory, filename + ".en.txt")
            extract_comments(source_file, output_file)

if __name__ == "__main__":
    directory_path = '.'
    process_directory(directory_path)