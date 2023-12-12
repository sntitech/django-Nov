from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Student, Teacher
from .constants import CLOUD_NAME, API_KEY, API_SECRET
import cloudinary
import cloudinary.uploader
import cloudinary.api

def home(request):
    return render(request, "home.html")


def contact(request):
    res = Teacher.objects.all().values()
    context = {
        "teachers": res
    }
    return HttpResponse(res)
    # return render(request, "contact.html", context=context)


def service(request):
    return render(request, "service.html")


def upload_image(request):
    """ 
        This function use to upload the file on cloudinary.
        Input : File
        Output : File Metadata
    """
    try:
        if request.method == 'POST' and request.FILES['myfile']:
            file_name = request.FILES['myfile']

            cloudinary.config( 
            cloud_name = CLOUD_NAME, 
            api_key = API_KEY, 
            api_secret = API_SECRET 
            )
            result = cloudinary.uploader.upload(file_name, 
            public_id = "natureImage")
            if result:
                context = {
                    "image_url": result.get("url")
                }
                return render(request, "home.html", context=context)
            return HttpResponse(f"File Uploaded. {result}")

    except Exception as ex:
        pass


def get_image():
    cloudinary.config( 
            cloud_name = CLOUD_NAME, 
            api_key = API_KEY, 
            api_secret = API_SECRET 
            )
    result = cloudinary.api.resource_by_asset_id("bdb9e574b51db707cd29984760d45cc2")
    print("==================",result.get('url'))

get_image()

# def upload_image():   
#     cloudinary.config( 
#     cloud_name = "damyuborr", 
#     api_key = "511947514892351", 
#     api_secret = "uE0AXqO3Z3KUDuc10WDaN4_fE38" 
#     )

#     result = cloudinary.uploader.upload("/Users/sagar/Documents/snti/repos/myproject/myapp/images/nature.jpeg", 
#     public_id = "mynature")
#     print(result)

# upload_image()


