"""
URL configuration for operation project.

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
from django.contrib import admin
from django.urls import path
from blogs.views import *
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('about/', about, name="about"),
    path('contact/', contact, name="contact"),
    path('write/', addBlog, name="addBlog"),
    path('viewBlog/<int:pk>', view_blog, name='viewBlog'),
    path('viewRegular/<int:pk>', viewRegular, name='viewRegular'),
    path('login/', log_in, name='login'),
    path('signup/', sign_up, name='signup'),
    path('reset/', reset, name='reset'),
    path('logout/', log_out, name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
