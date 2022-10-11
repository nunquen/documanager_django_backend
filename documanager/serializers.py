from rest_framework import serializers
from documanager.models import Document
from documanager.models import Revision
from documanager.models import User


class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = [
            "id",
            "name_s",
            "file_path_s",
            "file_name_s",
            "file_type_s",
            "url_s",
            "file_uploaded_b",
            "created_at_dt",
            "modified_at_dt",
            "revisions_i",
        ]
        ordering = ["revisions_i"]

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class RevisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Revision
        fields = [
            "id",
            "title_s",
            "comment_s",
            "number_i",
            "file_name_s",
            "file_type_s",
            "local_full_path_s",
            "file_uploaded_b",
            "created_at_dt",
            "modified_at_dt"
        ]
        ordering = ["-number_i"]