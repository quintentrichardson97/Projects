from django.db import models

# Create your models here.
class Skin(models.Model):
    artist= models.CharField(max_length=64, default="None")
    title = models.CharField(max_length=100, default="None")
    description = models.TextField(blank=True)
    skin = models.ImageField(upload_to='images/', default="None")

    def __str__(self):
        return f"{self.artist} created {self.title} DESCRIPTION: {self.description}"