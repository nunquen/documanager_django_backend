from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from documanager.models import User
from documanager.models import Document
from documanager.serializers import UserSerializer
from documanager.serializers import DocumentSerializer

@api_view(["GET"])
def user_list(request, format=None):
    if request.method == "GET": 
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

@api_view(["GET", "POST", "PUT", "DELETE"])
def single_user(request, id=None, format=None):
    try:
        user = User.objects.get(pk=id)
    except User.DoesNotExist:
        if request.method == "POST": 
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        else:
            return Response(status=status.HTTP_404_NOT_FOUND) 

    if request.method == "GET":
        serializer = UserSerializer(user)
        return Response(serializer.data)
    
    if request.method == "PUT":
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == "DELETE":
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(["GET"])
def document_list(request, id, format=None):
    try:
        user = User.objects.get(pk=id)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND) 
        
    if request.method == "GET": 
        document_list = Document.objects.filter(user=user)
        serializer = DocumentSerializer(document_list, many=True)
        return Response(serializer.data)

@api_view(["POST"])
def create_single_document(request, id, format=None):
    try:
        user = User.objects.get(pk=id)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "POST":
        request.data.update({"user_id": id})
        serializer = DocumentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)