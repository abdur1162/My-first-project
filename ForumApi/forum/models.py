from django.db import models

class Forum(models.Model):
    forum_id = models.AutoField(primary_key=True)
    forum_title = models.CharField(max_length=45)
    forum_description = models.TextField()
    forum_created_by = models.CharField(max_length=45)
    forum_created_on = models.DateTimeField(auto_now_add=True)
    forum_modified_on = models.DateTimeField(auto_now=True)
    forum_modified_by = models.CharField(max_length=45)

    def __str__(self):
        return self.forum_title

