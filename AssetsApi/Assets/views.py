from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Folder, File, RecycleBin
from .serializers import FolderSerializer, FileSerializer, RecycleBinSerializer, UserSerializer
from django.contrib.auth.models import User

class FolderViewSet(viewsets.ModelViewSet):
    queryset = Folder.objects.all()
    serializer_class = FolderSerializer

    def perform_create(self, serializer):
        user = self.request.user  # Get the currently authenticated user
        parent_folder_id = self.request.data.get('parent')  # Get the parent folder id
        parent_folder = Folder.objects.get(id=parent_folder_id) if parent_folder_id else None
        serializer.save(owner=user, parent=parent_folder)

    def perform_update(self, serializer):
        parent_folder_id = self.request.data.get('parent')  # Get parent folder if updating
        parent_folder = Folder.objects.get(id=parent_folder_id) if parent_folder_id else None
        serializer.save(parent=parent_folder)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class FolderViewSet(viewsets.ModelViewSet):
    queryset = Folder.objects.all()
    serializer_class = FolderSerializer

class FileViewSet(viewsets.ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer

    def move_file(self, request, pk):
        file = self.get_object()
        folder_id = request.data.get('folder_id')
        folder = Folder.objects.get(pk=folder_id)
        file.folder = folder
        file.save()
        return Response({'message': 'File moved successfully'})

    def share_file(self, request, pk):
        file = self.get_object()
        user_ids = request.data.get('user_ids', [])
        users = User.objects.filter(id__in=user_ids)
        file.shared_with.set(users)
        file.save()
        return Response({'message': 'File shared successfully'})

class RecycleBinViewSet(viewsets.ViewSet):
    def list(self, request):
        items = RecycleBin.objects.filter(owner=request.user)
        serializer = RecycleBinSerializer(items, many=True)
        return Response(serializer.data)

    def restore(self, request, pk):
        recycle_bin_item = RecycleBin.objects.get(pk=pk, owner=request.user)
        if recycle_bin_item.item_type == 'file':
            file = File.objects.get(pk=recycle_bin_item.item_id)
            file.folder = None  # Restore to root folder
            file.save()
        elif recycle_bin_item.item_type == 'folder':
            folder = Folder.objects.get(pk=recycle_bin_item.item_id)
            folder.parent = None  # Restore to root
            folder.save()
        recycle_bin_item.delete()
        return Response({'message': 'Item restored successfully'})

    def destroy(self, request, pk):
        recycle_bin_item = RecycleBin.objects.get(pk=pk, owner=request.user)
        if recycle_bin_item.item_type == 'file':
            File.objects.get(pk=recycle_bin_item.item_id).delete()
        elif recycle_bin_item.item_type == 'folder':
            Folder.objects.get(pk=recycle_bin_item.item_id).delete()
        recycle_bin_item.delete()
        return Response({'message': 'Item permanently deleted'})

