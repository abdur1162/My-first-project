from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FolderViewSet, FileViewSet, RecycleBinViewSet, UserViewSet

router = DefaultRouter()
router.register(r'folders', FolderViewSet, basename='folder')
router.register(r'files', FileViewSet, basename='file')
router.register(r'users', UserViewSet, basename='user')
urlpatterns = [
    path('', include(router.urls)),
    path('recycle-bin/', RecycleBinViewSet.as_view({'get': 'list'})),
    path('recycle-bin/<int:pk>/restore/', RecycleBinViewSet.as_view({'post': 'restore'})),
    path('recycle-bin/<int:pk>/delete/', RecycleBinViewSet.as_view({'delete': 'destroy'})),
    path('files/<int:pk>/move/', FileViewSet.as_view({'post': 'move_file'})),
    path('files/<int:pk>/share/', FileViewSet.as_view({'post': 'share_file'})),
]
