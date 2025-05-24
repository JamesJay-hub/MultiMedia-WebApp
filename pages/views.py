from django.shortcuts import render, redirect
from .models import MediaFile
from django.contrib.auth.decorators import login_required
from .forms import MediaUploadForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LogoutView

def index(request):
     return render(request, 'index.html')

@login_required
def media_list(request):
    # category = request.GET.get('category')
    # tag = request.GET.get('tag')
    media_files = MediaFile.objects.all()

    # if category:
    #         media_files = media_files.filter(categories__name=category)
    # if tag:
    #     media_files = media_files.filter(tags__name=tag)

    return render(request, 'media_list.html', {'media_files': media_files}) 

@login_required
def upload_media(request):
    if request.method == 'POST':
        form = MediaUploadForm(request.POST, request.FILES)
        if form.is_valid():
            media_file = form.save(commit=False)
            media_file.user = request.user  # Associate file with logged in user
            media_file.save()
            return redirect('media_list')   #redirect to media_list after successful upload
    else:
        form = MediaUploadForm()
    return render(request, 'upload.html', {'form': form })

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Saves the user data
            #Log thee user in after registration
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


        

    
