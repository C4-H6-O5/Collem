from django.db import models

class Asset(models.Model):
    file = models.FileField(upload_to='assets/')
    