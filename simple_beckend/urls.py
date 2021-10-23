from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from user_api import views
from memories_api.views import TagViewset, MemoryViewset
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('user', views.UserViewSet)
router.register('tag', TagViewset)
router.register('memory', MemoryViewset)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('login/', views.LoginView.as_view())

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
