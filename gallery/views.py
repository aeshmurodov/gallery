from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponseBadRequest
from .models import Image
from .forms import ImageForm
from django.views.decorators.csrf import csrf_exempt

def gallery(request):
    images = Image.objects.all()
    return render(request, 'gallery.html', {'images': images})

def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('gallery')
    else:
        form = ImageForm()
    return render(request, 'upload.html', {'form': form})

@csrf_exempt
def upload_image_api(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save()
            # Use build_absolute_uri with the image.url directly to avoid double slashes
            image_url = request.build_absolute_uri(image.image.url)
            return JsonResponse({
                'url': image_url,
                'message': 'Image uploaded successfully.'
            }, status=201)  # Return the URL of the uploaded image
        else:
            return JsonResponse({'error': form.errors}, status=400)
    return HttpResponseBadRequest("Invalid request method.")  # Handle non-POST requests

def api_instructions(request):
    return render(request, 'api_instructions.html', {'request': request})


def delete_image(request, pk):
    image = get_object_or_404(Image, pk=pk)
    if request.method == 'POST':
        image.delete()
        return redirect('gallery')
    return render(request, 'confirm_delete.html', {'image': image})
