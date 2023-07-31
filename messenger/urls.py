"""
URL configuration for 1123 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from chat.views import ChatViewset, redirect_view, AccountViewset

router = routers.DefaultRouter()
router.register(r'chats', ChatViewset)
router.register(r'accounts', AccountViewset)


urlpatterns = [
   path('admin/', admin.site.urls),
   path('api/', include(router.urls)),
   path('accounts/', include('django.contrib.auth.urls')),
   path('accounts/', include('accounts.urls')),
   path('chats/', include('chat.urls')),
   path('', redirect_view)
   #path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
