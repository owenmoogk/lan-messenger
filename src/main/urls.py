from django.contrib import admin
from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token
from chatMessages.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('token-auth/', obtain_jwt_token),
    path('users/', include('users.urls')),
    path('', include('frontend.urls')),
    path('sendMessage/', SendMessage.as_view()),
    path('getMessages/', getMessages)
]