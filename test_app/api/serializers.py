

from rest_framework import serializers


from rest_framework.serializers import ModelSerializer

from ..models import Blog
class BlogSerializer(ModelSerializer):
    class Meta:
        model = Blog
        fields = ['id' , 'name' , 'user' , 'amount' , 'description' ]
        read_only_fields = ['id']


from rest_framework import serializers


from rest_framework.serializers import ModelSerializer

from ..models import Comment
class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id' , 'user' , 'blog' , 'date' , 'description' ]
        read_only_fields = ['id']
