"""colorization URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path,include
from frontend import views
from django.conf import settings 
from django.conf.urls.static import static 
from frontend.views import image_upload
from django.contrib import admin
from django.urls import path,include
from frontend import views
from django.conf import settings
from django.conf.urls.static import static
from frontend.views import image_upload


urlpatterns = [
    path('admin/', admin.site.urls),             #for admin urls
    path('',include('frontend.urls')),           #for frontend app urls
    path('',views.index),                        #displaying default website i.e. index
    path('index/',views.index),                  #calling index function in case of index url
    path('upload/',image_upload,name="upload"),  #calling image_upload function in case of upload url
    path('upload/',views.index),                 #calling index function in case of upload url


   
    ]
if settings.DEBUG:
        urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
