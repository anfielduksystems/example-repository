from openai import OpenAI
client = OpenAI()
f=open(r"C:\Users\User\Documents\DevRepos\Ingredients.txt","r")
ingredients=f.read()
f.close()
response = client.responses.create(
    model="gpt-4.1-nano",
    input=f"""List the few recipes based on ingredients in the list below. For each recipe, provide a title and a short description.{ingredients}"""
)
print(response.output_text)