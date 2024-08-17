from g4f.client import Client
from g4f.Provider import BingCreateImages, OpenaiChat, Gemini
from g4f.cookies import set_cookies


client = Client(
    image_provider = BingCreateImages,

)

response = client.images.generate(
    model = "BingCreateImages",
    prompt = "a white siamese cat",
)

print(response.data[0].url)
