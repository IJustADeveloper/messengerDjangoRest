from django.db import models


class Account(models.Model):
    name = models.CharField(max_length=128)
    avatar = models.ImageField(upload_to='avatars', null=True)


class Chat(models.Model):
    name = models.CharField(max_length=256, unique=False)
    owner = models.ForeignKey(Account, on_delete=models.CASCADE)
    members = models.ManyToManyField(Account, related_name='member')


class Message(models.Model):
    text = models.CharField(max_length=512)
    sender = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)
    sent_time = models.DateTimeField(auto_now_add=True)
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
