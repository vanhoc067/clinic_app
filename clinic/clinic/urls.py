"""clinic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include

urlpatterns = [
    path('', include('clinicapp.urls')),
    path('admin/', admin.site.urls),
]

# from django.contrib import admin
# from django.urls import path, include
# from . import views
# from .admin import admin_site
# from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register('mesicine', views.ThuocViewSet)
# router.register('category_medicine', views.DanhMucViewSet)
# router.register('users', views.UserViewSet)
# router.register('hoadon',views.HoaDonViewSet)
# router.register('lichkham',views.LichKhamViewSet)


# urlpatterns = [
# path('', include(router.urls)),
# path(r'^ckeditor/', include('ckeditor_uploader.urls')),
# path('admin/',admin_site.urls)
# path('oauth2-info/',views.AuthInfo.as_view())

# ]
