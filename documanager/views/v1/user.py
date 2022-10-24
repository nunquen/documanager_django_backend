from django.db.utils import IntegrityError
from django.http.request import QueryDict
from documanager.models import User
from documanager.models import Document
from documanager.serializers import UserSerializer
from documanager.serializers import DocumentSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from typing import Dict


@api_view(["GET"])
def user_list(request:Request)->Response:
    """ Retrieve all users """
    if request.method == "GET": 
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

@api_view(["GET", "POST", "PUT", "DELETE"])
def single_user(request:Request, id:int)-> Response:
    """ Retrieve a sigle user by id """
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
def document_list(request:Request, id:int)-> Response:
    """ Retrieve all documents by user id """
    try:
        user = User.objects.get(pk=id)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND) 
        
    if request.method == "GET": 
        document_list = Document.objects.filter(user=user)
        serializer = DocumentSerializer(document_list, many=True)
        return Response(serializer.data)

@api_view(["POST"])
def create_single_document(request:Request, id:int)-> Response:
    """ Create a document for a User by user id """
    try:
        user = User.objects.get(pk=id)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "POST":
        """ In case we don't receive a dict object """
        if isinstance(request.data, QueryDict):
            request.data._mutable = True

        request.data.update({"user_id": id})
        serializer = DocumentSerializer(data=request.data)
        if serializer.is_valid():
            try:
                serializer.save(user=user)
            except IntegrityError as ie:
                status_code = 450
                error_msg = "duplicated url"

                if "documanager_document.file_uploaded_b" in str(ie):
                    status_code = 451
                    error_msg = "duplicated file name"
                
                return Response({"error": error_msg}, status=status_code )

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
