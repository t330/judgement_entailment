from django.db import models

# Create your models here.
class Sentence(models.Model):
    sentence1 = models.TextField()
    sentence2 = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self
