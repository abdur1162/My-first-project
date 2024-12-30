from django.db import models

class Post(models.Model):
    forum_id = models.IntegerField(null=True, blank=True)
    post_parent_id = models.IntegerField(null=True, blank=True)
    user_id = models.IntegerField()
    posts_content = models.TextField()
    posts_created_on = models.DateTimeField(auto_now_add=True)
    posts_created_by = models.CharField(max_length=45)
    posts_modified_on = models.DateTimeField(auto_now=True)
    posts_modified_by = models.CharField(max_length=45, null=True, blank=True)

    def __str__(self):
        return f"Post {self.id} by User {self.user_id}"
