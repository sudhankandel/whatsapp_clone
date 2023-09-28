from django.db import models
from django.contrib.auth.models import User
from chats.managers import ThreadManager


class ChatModel(models.Model):
    sender = models.CharField(max_length=100, default=None)
    message = models.TextField(null=True, blank=True)
    thread_name = models.CharField(null=True, blank=True, max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.message


class TrackingModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Thread(TrackingModel):
    name = models.CharField(max_length=50, null=True, blank=True)
    users = models.ManyToManyField('auth.User')

    objects = ThreadManager()

    def __str__(self) -> str:
        return f'{self.users.first()} and {self.users.last()}'

class Message(TrackingModel):
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    sender = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    text = models.TextField(blank=False, null=False)

    def __str__(self) -> str:
        return f'From <Thread - {self.thread}>'
    

