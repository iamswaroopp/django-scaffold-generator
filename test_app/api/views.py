

from rest_framework import viewsets


from rest_framework.viewsets import ModelViewSet


from rest_framework.permissions import DjangoModelPermissions


from ..models import Blog
from .serializers import BlogSerializer

class BlogViewset(ModelViewSet):
    permission_classes = [ DjangoModelPermissions ]
    serializer_class = BlogSerializer

    def get_queryset(self):
        return Blog.objects.all()



from rest_framework import viewsets


from rest_framework.viewsets import ModelViewSet


from rest_framework.permissions import DjangoModelPermissions


from ..models import Comment
from .serializers import CommentSerializer

class CommentViewset(ModelViewSet):
    permission_classes = [ DjangoModelPermissions ]
    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.all()

