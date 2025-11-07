from bs4 import BeautifulSoup
import requests
from openai import OpenAI

client = OpenAI()

# Step 1: Scrape the page and extract paragraphs
url = "https://www.deeplearning.ai/the-batch/announcing-the-deeplearning-ai-pro-membership/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

paragraphs = [p.get_text(strip=True) for p in soup.find_all("p")]
text_block = "\n".join(paragraphs)

# Step 2: Pass to LLM for bullet-point summary
summary_response = client.chat.completions.create(
    model="gpt-5-mini",
    messages=[
        {"role": "system", "content": "You summarize web content into clear bullet points."},
        {"role": "user", "content": f"""Summarize the following text into concise bullet points:

{text_block}
"""}
    ]
)

# Step 3: Print the bullet summary
print("\n🔹 Summary of the Page:\n")
print(summary_response.choices[0].message.content.strip())