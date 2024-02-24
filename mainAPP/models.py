from django.db import models

from django.contrib.auth.models import User


class Tasks(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=50, choices=(
        ("No started", "No started"),
        ('In progress', 'In progress'),
        ('Completed', 'Completed')
    ))
    created_at = models.DateField(auto_now_add=True)
    deadline = models.DateField()

    def __str__(self):
        return f"{self.user.username}: {self.title}"
