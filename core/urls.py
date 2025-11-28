from django.urls import path,include
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from rest_framework.routers import DefaultRouter
from . import views
from .views import NoteViewSet
router = DefaultRouter()
router.register("",NoteViewSet)
from drf_spectacular.views import SpectacularAPIView,SpectacularSwaggerView
from rest_framework import permissions

urlpatterns = [
    path('h/',views.HelloView.as_view(),name="hello"),
    path('api/', include(router.urls)),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('refresh/', TokenRefreshView.as_view(), name='refresh'),
    path('api/schema/', SpectacularAPIView.as_view(permission_classes=[permissions.AllowAny]), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(permission_classes=[permissions.AllowAny]), name='swagger-ui'),
    
    
]

