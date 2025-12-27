from django.db import models

# 1. THE TAG MODEL
class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    normalized_name = models.CharField(max_length=50, unique=True, editable=False)

    def save(self, *args, **kwargs):
        self.normalized_name = self.name.lower()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

# 2. THE ASSET MODEL (The Parent)
class Asset(models.Model):
    class Status(models.TextChoices):
        PENDING = 'PENDING', 'Pending'
        PROCESSING = 'PROCESSING', 'Processing'
        READY = 'READY', 'Ready'

    file = models.FileField(upload_to='assets/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20, 
        choices=Status.choices, 
        default=Status.PENDING
    )
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return f"Asset({self.id}) - {self.status}"

# 3. THE IMAGE MODEL (Inherits from Asset)
class Image(Asset):
    width = models.IntegerField(null=True, blank=True)
    height = models.IntegerField(null=True, blank=True)
    camera_model = models.CharField(max_length=100, blank=True)
    iso = models.CharField(max_length=20, blank=True)

# 4. THE VIDEO MODEL (Inherits from Asset)
class Video(Asset):
    duration = models.FloatField(help_text="Duration in seconds", null=True, blank=True)
    fps = models.FloatField(null=True, blank=True)
    codec = models.CharField(max_length=50, blank=True)