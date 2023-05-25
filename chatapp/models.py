from django.db import models

class ChatMessage(models.Model):
    message = models.TextField()
    media = models.FileField(upload_to='media/', blank=True, null=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"ChatMessage {self.pk}"
