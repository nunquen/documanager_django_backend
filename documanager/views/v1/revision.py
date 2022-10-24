from documanager.models import Revision
from documanager.serializers import RevisionSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

@api_view(["GET", "PUT"])
def single_revision(request:Request, id:int)->Response:
    try:
        document = Revision.objects.get(pk=id)
    except Revision.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND) 

    if request.method == "GET":
        serializer = RevisionSerializer(document)
        return Response(serializer.data)