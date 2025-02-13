from django.db import models
from django.contrib.auth.models import User

PRIORITY = (
    ('1', '高'),
    ('2', '中'),
    ('3', '低'),
)

class Task(models.Model):
    title = models.CharField(max_length=100)
    status = models.BooleanField(default=False)
    priority = models.CharField(
        max_length = 1,
        choices = PRIORITY
    )
    deadline = models.DateTimeField()
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.PROTECT, default=1)

    def __str__(self):
        return self.title
