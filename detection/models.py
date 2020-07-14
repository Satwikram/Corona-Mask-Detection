from django.db import models

# Create your models here.
class detect(models.Model):
    media_path = models.CharField(max_length = 200, null=True)
