from g4f.client import Client

client = Client()
inputText = """"""

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": inputText}],

    )

print(response.choices[0].message.content)


