from django.core.files import File
from core.models import Asset

def save_asset(file_path):
    with open(file_path, 'rb') as f:
        django_file = File(f)
        asset = Asset.objects.create(file=django_file)
    return asset

