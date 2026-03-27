
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('blogdetails/', include('django.contrib.auth.urls')),
    path('blogdetails/', include('blogdetails.urls')),
]
