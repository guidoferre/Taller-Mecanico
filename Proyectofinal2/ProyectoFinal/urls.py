from django.contrib import admin
from django.urls import path
from blog import views
from blog.views import inicio
from blog.views import cliente
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    
]
