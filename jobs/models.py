from django.db import models

# Create your models here.
class Job(models.Model):
    image=models.ImageField(upload_to='images/')
    summary=models.CharField(max_length=2000)
    detail=models.TextField()
    url_field = models.URLField(max_length=200)

    def __str__(self):
        return self.summary