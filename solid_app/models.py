
# Create your models here.
# solid_app/models.py
from django.db import models

class TextFile(models.Model):
    content = models.TextField()
