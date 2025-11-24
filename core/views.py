from django.shortcuts import render
from  rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .serializers import NoteSerializer
from rest_framework.permissions import IsAuthenticated,BasePermission
from .models import Note
from drf

class HelloView(APIView):
    def get(self,request):
        return Response({"text":"salom"})
    
# class IsOwner(BasePermission):
#     def has_object_permission(self, request, view, obj):
#         return obj.owner == request.user
    
class NoteViewSet(ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        return super().perform_create(serializer)
    
    
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)
    
    
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
