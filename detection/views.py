import os

from django.core.files.storage import FileSystemStorage
from django.shortcuts import render

# Create your views here.
from detection.models import detect


def upload(request):

    if request.method == 'POST':

        try:
            folder = 'media/images/'
            uploaded_image = request.FILES['cd']
            print("NAME IS:", uploaded_image.name)

            filename = str(uploaded_image.name)
            fs = FileSystemStorage(location = folder)
            name = fs.save(uploaded_image.name, uploaded_image)
            mediapath = folder + "{}"
            filepath = os.path.join(mediapath).format(name)
            print(filepath)

            mask_images = detect()
            mask_images.media_path = filepath
            mask_images.save()

        except:
            pass


    else:
         return render(request, 'upload.html')
