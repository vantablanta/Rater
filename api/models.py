from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    image = CloudinaryField('image', blank = True)
    description = models.TextField(blank=True)
    url = models.URLField(max_length=300)

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    profile_photo = CloudinaryField("image", blank= True)
    bio = models.TextField(blank=True)
    projects = models.ForeignKey(Post, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)


