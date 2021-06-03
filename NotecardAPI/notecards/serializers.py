from rest_framework import serializers
from .models import Collection
from .models import Notecard


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['name']


class NotecardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notecard
        fields = ['id', 'word', 'definition', 'collection']
