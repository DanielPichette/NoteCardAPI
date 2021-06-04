from django.shortcuts import render

# Create your views here.
from django.http import Http404
from django.shortcuts import render
from .models import Collection
from .models import Notecard
from .serializers import CollectionSerializer
from .serializers import NotecardSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
class Collections(APIView):

    def get(self, request):
        collection = Collection.objects.all()
        serializer = CollectionSerializer(collection, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = CollectionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Notecards(APIView):

    def get(self, request):
        notecard = Notecard.objects.all()
        serializer = NotecardSerializer(notecard, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = NotecardSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CollectionById(APIView):
    def get_object(self, pk):
        try:
            return Collection.objects.get(pk=pk)
        except Collection.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        collection = self.get_object(pk)
        serializer = CollectionSerializer(collection)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        collection = self.get_object(pk)
        serializer = CollectionSerializer(collection, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        collection = self.get_object(pk)
        collection.delete()
        return Response(status=status.HTTP_200_OK)


class NotecardById(APIView):
    def get_object(self, pk):
        try:
            return Notecard.objects.get(pk=pk)
        except Notecard.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        notecard = self.get_object(pk)
        serializer = NotecardSerializer(notecard)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        notecard = self.get_object(pk)
        serializer = NotecardSerializer(notecard, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        notecard = self.get_object(pk)
        notecard.delete()
        return Response(status=status.HTTP_200_OK)
