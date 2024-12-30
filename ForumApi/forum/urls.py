from rest_framework.routers import DefaultRouter
from django.urls import path, include
from forum.views import ForumViewSet

router = DefaultRouter()
router.register(r'forum', ForumViewSet, basename='forum')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
