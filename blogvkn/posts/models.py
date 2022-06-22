from audioop import reverse
from distutils.command.upload import upload
from django.db import models
from django.urls import reverse


# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=99)
    content = models.TextField(max_length=700)
    image = models.ImageField(null=True, blank=True, upload_to='images')
    jumlah = models.IntegerField(null=True)
    date = models.DateField(auto_now_add=True)
    # slug = models.SlugField(max_length=191, unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', kwargs={'id': self.id})
