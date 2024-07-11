import openai
import os

# Set up your OpenAI API key
#openai.api_key = 'your-openai-api-key'
openai.api_key=''


def translate_content(text, model="gpt-3.5-turbo", max_tokens=500):

    user_message=f"""
Please reply to the text fragments, from Dutch to english, keep formatting, including whitespace:
{text}
"""

    response = openai.ChatCompletion.create(
        model=model,
        messages = [ {"role": "system", "content": "You are a helpful translater"},
            {"role": "user", "content": user_message } ],
        max_tokens=max_tokens,
        temperature=0.7,
    ) 
    translated_content = response.choices[0].message['content'].strip()
    return translated_content

def translate_file(nl_file, en_file):
    with open(nl_file, "r", encoding="utf-8") as file:
        nl_comments = [comment.strip() for comment in file.read().split("\n\n")]

    with open(en_file, "w", encoding="utf-8") as file:
        for nl_comment in nl_comments:
            if nl_comment:
                translated_comment = translate_content(nl_comment)
                file.write(translated_comment + "\n\n")
                print(f"Translated strings: {nl_comment} to {translated_comment}")

def process_directory(directory):
    for filename in os.listdir(directory):
        if filename.endswith("strings.nl.txt"):
            nl_file = os.path.join(directory, filename)
            en_file = os.path.join(directory, filename.replace(".nl.txt", ".en.txt"))
            translate_file(nl_file, en_file)

if __name__ == "__main__":
    directory_path = "."
    process_directory(directory_path)

