
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Note
from .serializers import NoteSerializer
# Create your views here.

@api_view(['GET'])
def getRoutes(request):
    
    routes = [
        {
            'Endpoint':'/notes/',
            'method':'GET',
            'body':None ,
            'description':'return a body of notes'
        },
          {
            'Endpoint':'/notes/id',
            'method':'GET',
            'body':None ,
            'description':'return a single of notes objects'
        },
         {
            'Endpoint':'/notes/create',
            'method':'POST',
            'body':{"body":""},
            'description':'create new notes with data sent it post request'
        },
        {
            'Endpoint':'/notes/id/update',
            'method':'PUT',
            'body':{"body":""},
            'description':'create new notes with data sent it put request'
        },
        {
            'Endpoint':'/notes/id/delete',
            'method':'DELETE',
            'body':None,
            'description':'Delete object '
        },
    ]
    
    return Response(routes)

@api_view(['GET'])
def getNotes(request):
    notes = Note.objects.all()
    serializer = NoteSerializer(notes,many = True)
    return Response(serializer.data)


@api_view(['GET'])
def getNote(request,pk):
    notes = Note.objects.get(id=pk)
    serializer = NoteSerializer(notes,many = False)
    return Response(serializer.data)
