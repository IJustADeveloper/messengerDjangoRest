from django.contrib.auth.models import User
from django.db import models


class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    avatar = models.ImageField(upload_to='avatars', null=True, default="avatars/default.jpg")


class Chat(models.Model):
    name = models.CharField(max_length=256, unique=False)
    owner = models.ForeignKey(Account, on_delete=models.CASCADE)
    members = models.ManyToManyField(Account, related_name='member')


class Message(models.Model):
    text = models.CharField(max_length=512)
    sender = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)
    sent_time = models.DateTimeField(auto_now_add=True)
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)

    @staticmethod
    def messages_preload(chat_id):
        qs = Message.objects.filter(chat=chat_id).order_by("-sent_time")[:10]
        s = []
        for q in range(len(qs)-1, -1, -1):
            s.append(qs[q].sender.name + ": " + qs[q].text)

        return "\n".join(s)
