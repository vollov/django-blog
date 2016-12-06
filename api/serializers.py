from django.contrib.auth.models import User, Group
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    # optional
    # groups = serializers.PrimaryKeyRelatedField(many=True, queryset=Group.objects.all())
    
    class Meta:
        model = User
        fields = ('pk', 'url', 'username','password', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')