from django.contrib.auth.models import User
from django.db import models
import uuid


class Group(models.Model):
    name = models.CharField(max_length=100)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_groups')
    join_link = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    members = models.ManyToManyField(User, through='Membership', through_fields=('group', 'user'))

    def __str__(self):
        return self.name


class Membership(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    join_token = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)

    def __str__(self):
        return f'{self.user} in {self.group}'


class Task(models.Model):
    LOW = 1
    MEDIUM = 2
    HIGH = 3

    PRIORITY_CHOICES = (
        (LOW, 'Low'),
        (MEDIUM, 'Medium'),
        (HIGH, 'High'),
    )
    
    CATEGORY_CHOICES = (
        ("Work", "Work"),
        ("Personal", "Personal"),
        ("Shopping", "Shopping"),
        ("Household", "Household"),
        ("Education", "Education"),
        ("Fitness", "Fitness"),
        ("Other", "Other"),
    )

    title = models.CharField(max_length=200)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_tasks', default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    deadline = models.DateTimeField(null=True, blank=True)
    priority = models.IntegerField(choices=PRIORITY_CHOICES, default=MEDIUM)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default="Other")
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, blank=True, related_name='tasks')

    class Meta:
        ordering = ['complete', '-created_at']

    def __str__(self):
        return self.title