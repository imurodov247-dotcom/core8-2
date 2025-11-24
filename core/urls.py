from django.urls import path,include
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from rest_framework.routers import DefaultRouter
from . import views
from .views import NoteViewSet
router = DefaultRouter()
router.register("",NoteViewSet)


urlpatterns = [
    path('h/',views.HelloView.as_view(),name="hello"),
    path('api/', include(router.urls)),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('refresh/', TokenRefreshView.as_view(), name='refresh'),
]

