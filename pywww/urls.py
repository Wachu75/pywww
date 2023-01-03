"""pywww URL Configuration

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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from App import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #  path('main/', include('main.urls')),
    path('books/', include('books.urls')),
    path('posts/', include('posts.urls')),
    path('galleries/', include('galleries.urls')),
    path('', include('main.urls')),
    #path('', include('register.urls')),
    path('account/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
    path('create/', views.data_form, name='data_create'),
    path('data/', views.data_read, name='data_read'),
    path('<int:id>', views.data_form, name='data_update'),
    path('data_delete/<str:candidate_id>', views.data_delete, name='data_delete'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


#urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)