from django.shortcuts import render
from  rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .serializers import NoteSerializer
from rest_framework.permissions import IsAuthenticated,BasePermission
from .models import Note
from drf_spectacular.utils import extend_schema

class HelloView(APIView):
    def get(self,request):
        return Response({"text":"salom"})
    
# class IsOwner(BasePermission):
#     def has_object_permission(self, request, view, obj):
#         return obj.owner == request.user
    

  
    
class NoteViewSet(ModelViewSet):
    """
    CRUD operations for authenticated user notes
    """
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        return super().perform_create(serializer)
    
    @extend_schema(
        summary="Bitta obyektni olish"
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
      
    @extend_schema(
        summary=" obyektni yaratish"
    )  
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
      
    @extend_schema(
        summary="Obyektni toliq yangilash"
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
      
    @extend_schema(
        summary="Qisman yangilash"
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)
    
      
    @extend_schema(
        summary="Ochirish"
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
