from helper_functions import list_files, upload_text_file
from openai import OpenAI
import os

client = OpenAI()
directory = "C:/Users/User/Documents/DevRepos"
files = list_files(directory)

html_output = "<html><body>\n"

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

    # Format HTML block
    html_output += f'<h2 style="color:blue;"><b>{filename}</b></h2>\n'
    html_output += "<ul>\n"
    for line in dish_response.choices[0].message.content.strip().splitlines():
        if line.startswith("-"):
            html_output += f"<li>{line[1:].strip()}</li>\n"
    html_output += "</ul>\n"

html_output += "</body></html>"

# Print final HTML
print(html_output)

# Save HTML to file
output_path = os.path.join(directory, "best_dishes.html")
with open(output_path, "w", encoding="utf-8") as html_file:
    html_file.write(html_output)
print(f"\n✅ HTML file saved to: {output_path}")