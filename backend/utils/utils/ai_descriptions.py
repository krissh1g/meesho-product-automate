import openai

openai.api_key = "YOUR_OPENAI_KEY"

def generate_description(title):
    prompt = f"Write a Meesho-ready product description in bullets for {title}."
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=80
    )
    return response.choices[0].text.strip()
