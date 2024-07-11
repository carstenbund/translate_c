def create_mapping_file(nl_file, en_file, output_file):
    with open(nl_file, "r", encoding="utf-8") as file_nl:
        nl_strings = [line.strip() for line in file_nl.readlines()]

    with open(en_file, "r", encoding="utf-8") as file_en:
        en_strings = [line.strip() for line in file_en.readlines()]

    if len(nl_strings) != len(en_strings):
        raise ValueError("The number of lines in the Strings files do not match.")

    with open(output_file, "w", encoding="utf-8") as file_out:
        for nl_string, en_string in zip(nl_strings, en_strings):
            file_out.write(f"{nl_string}|||{en_string}\n")

    print(f"Mapping file created: {output_file}")

if __name__ == "__main__":
    nl_file = "path/to/your/en_strings.txt"
    en_file = "path/to/your/jp_strings.txt"
    output_file = "path/to/your/mapping_file.txt"
    create_mapping_file(nl_file, en_file, output_file)

