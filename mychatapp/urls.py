from django.contrib import admin
from django.urls import path,include

urlpatterns = [   
    path('chats/', include('chatapp.urls')), 
    path('admin/', admin.site.urls),
]
