from django.contrib import admin
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import include, url
from chatMessages.views import homeView

urlpatterns = [
    path("", homeView),
    path("home/", homeView),
    path('admin/', admin.site.urls),
    url(r"^", include("users.urls")),
]

urlpatterns += staticfiles_urlpatterns()