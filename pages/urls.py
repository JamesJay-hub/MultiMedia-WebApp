from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
# from .views import media_list, upload_media

urlpatterns = [
    path('', views.index, name='index'),
    path('media', views.media_list, name='media_list'),
    path('upload/', views.upload_media, name='upload_media'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),  
    path('logout/', LogoutView.as_view(), name='logout'),  
    path('register/', views.register, name='register'),  

]
# template_name='login.html'