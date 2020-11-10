from rest_framework import generics

from snippets.models import Snippet
from snippets.serializers import SnippetSerializer

"""
serializer = SnippetSerializer(data=request.data)
=> request는 JSON type, But .data가 parsed content를 반환!
"""


class SnippetList(generics.ListCreateAPIView):

    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer