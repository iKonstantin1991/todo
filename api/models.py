from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

statuses = (
    (1, 'New'),
    (2, 'In progress'),
    (3, 'Done')
)
default_status = 1


class Task(models.Model):
    name = models.CharField(
        'Name',
        max_length=150,
    )
    description = models.TextField()
    created = models.DateTimeField(
        auto_now_add=True,
    )
    do_until = models.DateField()
    status = models.SmallIntegerField(choices=statuses)
    responsible = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='tasks_responsible',
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='task_author'
    )

    class Meta:
        ordering = ['do_until', 'status']

    def __str__(self):
        return self.name
