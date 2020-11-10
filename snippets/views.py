from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework import permissions

from snippets.models import Snippet
from snippets.serializers import SnippetSerializer, UserSerializer

"""
serializer = SnippetSerializer(data=request.data)
=> request는 JSON type, But .data가 parsed content를 반환!
"""


class SnippetList(generics.ListCreateAPIView):

    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    """
    The user isn't sent as part of the serialized representation, 
    but is instead a property of the incoming request.
    """

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
