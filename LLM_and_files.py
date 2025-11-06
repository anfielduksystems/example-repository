from helper_functions import list_files, upload_text_file
from openai import OpenAI
import os

client = OpenAI()
directory = "C:/Users/User/Documents/DevRepos"
files = list_files(directory)

for filename in files:
    filepath = os.path.join(directory, filename)
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Step 1: Check relevance
    relevance_response = client.chat.completions.create(
        model="gpt-5-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that checks document relevance."},
            {"role": "user", "content": f'Respond with "Relevant" or "Not Relevant" based on whether the document describes restaurants:\n{content}'}
        ]
    )

    verdict = relevance_response.choices[0].message.content.strip()
    if verdict != "Relevant":
        continue

    # Step 2: Extract best dishes
    dish_response = client.chat.completions.create(
        model="gpt-5-mini",
        messages=[
            {"role": "system", "content": "You extract the best dishes mentioned in restaurant-related documents."},
            {"role": "user", "content": f"""From the following text, list the best dishes mentioned. 
Return them as a simple bullet list. If possible, include the restaurant name and city if available.

Text:
{content}
"""}
        ]
    )

    print(f"\n Best Dishes in {filename}:\n{dish_response.choices[0].message.content.strip()}")