from rest_framework import generics

from .models import Tag
from .serializers import TagSerializer


class TagView(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class TagCreate(generics.CreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class TagRetrieve(generics.RetrieveAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
