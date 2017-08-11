from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from users.models import PopoFoo
from users.serializers import PopoFooSerializer


class PopoFooList(APIView):
    """
    List all snippets, or create a new snippet.
    """

    def get(self, request, format=None):
        elements = [
            PopoFoo(),
            PopoFoo(),
            PopoFoo(),
            PopoFoo()
        ]
        serializer = PopoFooSerializer(elements, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PopoFooSerializer(data=request.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
