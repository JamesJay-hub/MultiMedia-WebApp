from django.db import models
from django.contrib.auth.models import User


# class Category(models.Model):
#     name = models.CharField(max_length=100)

# class Tag(models.Model):
#     name = models.CharField(max_length=50)

class MediaFile(models.Model):
    MEDIA_TYPES = [('image', 'Image'), ('video', 'Video'), ('audio', 'Audio')]
    
    title = models.CharField(max_length=255)
    media_type = models.CharField(choices=MEDIA_TYPES, max_length=10)
    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    # categories = models.ManyToManyField(Category)
    # tags = models.ManyToManyField(Tag)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} - {self.user.username}"
    

    # class Registration(models.Model):
    #     username = models.CharField(max_length=30)
    #     email = models.EmailField(100)
    #     password = models.CharField(widget=models.PasswordInput)
    #     confirm_password = models.CharField(widget=models.PasswordInput)


    


        

