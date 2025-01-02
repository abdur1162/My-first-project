"""
URL configuration for AssetsProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static

# Import the routers from your app
from Assets.views import FolderViewSet, FileViewSet, RecycleBinViewSet, UserViewSet

# Set up the router for the API
router = DefaultRouter()
router.register(r'folders', FolderViewSet, basename='folder')
router.register(r'files', FileViewSet, basename='file')
router.register(r'users', UserViewSet, basename='user') 



urlpatterns = [
    # Admin panel
    path('admin/', admin.site.urls),

    # Include the app's API URLs
    path('api/', include(router.urls)),

    # Recycle Bin custom endpoints
    path('api/recycle-bin/<int:pk>/restore/', RecycleBinViewSet.as_view({'post': 'restore'}), name='restore-item'),
    path('api/recycle-bin/<int:pk>/delete/', RecycleBinViewSet.as_view({'delete': 'destroy'}), name='delete-item'),
    
    # Additional file actions
    path('api/files/<int:pk>/move/', FileViewSet.as_view({'post': 'move_file'}), name='move-file'),
    path('api/files/<int:pk>/share/', FileViewSet.as_view({'post': 'share_file'}), name='share-file'),
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

