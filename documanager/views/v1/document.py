import os
from documanager.settings import MEDIA_ROOT, MEDIA_FOLDER
from documanager.models import Document
from documanager.models import Revision
from documanager.serializers import DocumentSerializer
from documanager.serializers import RevisionSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(["GET", "PUT"])
def single_document(request, id, format=None):
    try:
        document = Document.objects.get(pk=id)
    except Document.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND) 

    if request.method == "GET":
        serializer = DocumentSerializer(document)
        return Response(serializer.data)

    if request.method == "PUT":
        serializer = DocumentSerializer(document, serializer.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == "DELETE":
        document.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(["POST"])
def create_single_revision(request, id, format=None):
    try:
        document = Document.objects.get(pk=id)
    except Document.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "POST":
        request.data.update({"document_id": id})
        serializer = RevisionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(document=document)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
def revision_list(request, id, format=None):
    try:
        document = Document.objects.get(pk=id)
    except Document.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND) 
        
    if request.method == "GET": 
        revision_list = Revision.objects.filter(document=document)
        serializer = RevisionSerializer(revision_list, many=True)
        return Response(serializer.data)
