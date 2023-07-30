from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.views.generic import ListView
from rest_framework import viewsets
from rest_framework import permissions


from .serializers import *
from .models import *


class ChatViewset(viewsets.ModelViewSet):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer


class ChatsView(LoginRequiredMixin, ListView):
    model = Chat
    template_name = 'chats.html'
    context_object_name = 'chats'

    def get_queryset(self):
        queryset = []
        if self.request.user.is_authenticated:
            cur_account = Account.objects.filter(user=self.request.user)
            queryset = Chat.objects.filter(members__in=cur_account)
            # self.filterset = PostFilter(self.request.GET, queryset)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


def chatView(request, chat_id):
    try:
        chat_room = Chat.objects.get(id=chat_id)
        return render(request, 'chat.html', {'chat': chat_room, 'msg': '', 'preload': Message.messages_preload(chat_room.id)+"\n"})
    except ObjectDoesNotExist:
        return render(request, 'chat.html', {'chat': None, 'msg': 'Chat with this id does not exist.'})




