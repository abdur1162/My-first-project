from django.db import models
from django.contrib.auth.models import User

class Folder(models.Model):
    name = models.CharField(max_length=255)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='subfolders')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class File(models.Model):
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='files/')
    folder = models.ForeignKey(Folder, null=True, blank=True, on_delete=models.CASCADE, related_name='files')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    shared_with = models.ManyToManyField(User, related_name='shared_files', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class RecycleBin(models.Model):
    item_type = models.CharField(max_length=50, choices=[('file', 'File'), ('folder', 'Folder')])
    item_id = models.PositiveIntegerField()
    deleted_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.item_type} {self.item_id} by {self.owner}"
