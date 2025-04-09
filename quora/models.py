from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Question(models.Model):
    user       = models.ForeignKey(User, on_delete=models.CASCADE)
    title      = models.CharField(max_length=255)
    body       = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Answer(models.Model):
    user       = models.ForeignKey(User, on_delete=models.CASCADE)
    question   = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    body       = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[:50]
    
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE, related_name='likes')

    class Meta:
        unique_together = ('user', 'answer')  # prevent multiple likes