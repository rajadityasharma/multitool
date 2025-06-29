from django.shortcuts import render
from rembg import remove
from PIL import Image, ImageEnhance
import io
import base64
from django.shortcuts import redirect

def background_remover(request):
    image_data = None

    if request.method == 'POST':
        uploaded_file = request.FILES.get('image')
        if uploaded_file:
            try:
                input_image = Image.open(uploaded_file)
                output_image = remove(input_image)

                buffer = io.BytesIO()
                output_image.save(buffer, format='PNG')
                buffer.seek(0)
                image_data = base64.b64encode(buffer.read()).decode('utf-8')

            except Exception as e:
                print("Error in processing image:", e)
                # Optional: You can return an error page here too
        else:
            print("No file uploaded")

    return render(request, 'background_remover.html', {'image_data': image_data})


def home(request):
    return redirect('remove_bg')  

def image_enhancer(request):
    enhanced_image = None

    if request.method == 'POST' and request.FILES.get('image'):
        uploaded_file = request.FILES['image']
        image = Image.open(uploaded_file)

        # Enhance the image
        enhancer_brightness = ImageEnhance.Brightness(image)
        image = enhancer_brightness.enhance(1.3)

        enhancer_contrast = ImageEnhance.Contrast(image)
        image = enhancer_contrast.enhance(1.3)

        enhancer_sharpness = ImageEnhance.Sharpness(image)
        image = enhancer_sharpness.enhance(2.0)

        # Convert to base64
        buffer = io.BytesIO()
        image.save(buffer, format='PNG')
        buffer.seek(0)
        enhanced_image = base64.b64encode(buffer.read()).decode('utf-8')

    return render(request, 'image_enhancer.html', {'enhanced_image': enhanced_image})