
from openai import OpenAI
from django.conf import settings

client = OpenAI(api_key=settings.OPENAI_API_KEY)

def generate_image(prompt):
    response = client.images.generate(
    model="dall-e-3",
    prompt=prompt,
    size="1024x1024",  # Use a valid size, like 512x512 or 1024x1024
    quality="standard",
    n=1,
    )
    return response.data[0].url
