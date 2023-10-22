import requests
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Profile
from .serializer import ProfileSerializer


@api_view(['GET', 'POST'])
def ProfileList(request):
    if request.method == 'GET':
        prof = Profile.objects.all()
        serializer = ProfileSerializer(prof, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def ProfileDetails(request, id):
    try:
        prof = Profile.objects.get(pk=id)
    except Profile.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProfileSerializer(prof)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ProfileSerializer(prof, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        prof.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


def profile_list_view(request):
    api_url = 'http://127.0.0.1:8000/api/profile/'
    # api_url = 'http://192.168.0.126:8080/api/profile/'
    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()
    else:
        data = []

    return render(request, 'index.html', {'data': data})
