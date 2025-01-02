from rest_framework import serializers
from .models import Folder, File, RecycleBin, User
from django.contrib.auth.models import User

class FolderSerializer(serializers.ModelSerializer):
    owner_name = serializers.CharField(source='owner.username', read_only=True)  # For showing owner name
    parent_folder_name = serializers.CharField(source='parent.name', read_only=True, required=False)  # For showing parent folder name

    class Meta:
        model = Folder
        fields = ['id', 'name', 'parent', 'owner', 'owner_name', 'parent_folder_name']

    def create(self, validated_data):
        # Automatically assign the current user as the owner
        owner = self.context['request'].user
        parent_folder = validated_data.get('parent', None)  # Optional parent folder
        folder = Folder.objects.create(owner=owner, parent=parent_folder, **validated_data)
        return folder

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']


class FolderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Folder
        fields = ['id', 'name', 'parent', 'owner', 'created_at']

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ['id', 'name', 'file', 'folder', 'owner', 'shared_with', 'created_at']

class RecycleBinSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecycleBin
        fields = ['id', 'item_type', 'item_id', 'deleted_at', 'owner']
