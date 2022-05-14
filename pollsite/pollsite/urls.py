from django.contrib import admin
from django.urls import path, include
from polls import urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('polls/', include('polls.urls')),
    path('user/', include('users.urls')),
]
