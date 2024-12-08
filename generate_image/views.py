
from django.shortcuts import render
from .ai_image import generate_image

def generate_image_view(request):
    image_url = None
    if request.method == "POST":
        prompt = request.POST.get('prompt')
        if prompt:
            image_url = generate_image(prompt)
    return render(request, 'image_generator/generate_image.html', {'image_url': image_url})