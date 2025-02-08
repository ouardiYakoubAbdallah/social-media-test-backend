from django.db import models


class Post(models.Model):
    content = models.TextField(blank=False, null=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        to='authentication_and_authorization.User',
        on_delete=models.CASCADE,
        related_name='posts'
    )

    def __str__(self):
        return f"Post by {self.author.username} at {self.timestamp}"
