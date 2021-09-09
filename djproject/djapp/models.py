from django.db import models
from django.contrib.auth.models import User


class BlogModel(models.Model):
    title_tag=models.CharField(max_length=100)
    title=models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images',blank=True,default='m.jpg')
    description=models.TextField()
    dt=models.DateField(auto_now_add=True)






