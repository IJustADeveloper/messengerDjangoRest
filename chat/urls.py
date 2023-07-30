from django.urls import path

from chat.views import ChatsView, chatView

urlpatterns = [
    path('', ChatsView.as_view(), name='chats'),
    path('<int:chat_id>', chatView, name='chat'),
]