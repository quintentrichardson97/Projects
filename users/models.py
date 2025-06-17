from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=64, default="None")
    first_name = models.CharField(max_length=64, default="None")
    last_name = models.CharField(max_length=64, default="None")
    birthday = models.DateTimeField(auto_now_add=True)
    user_type = models.CharField(max_length=64)
    profile_picture = models.ImageField(upload_to='profile_images/', default="None")
    user_key = models.CharField(max_length=64, default="None")

    def __str__(self):
        return self.name

