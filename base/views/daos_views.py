from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from base.models.daos_models import *
from base.serializers.daos_serializer import *


@api_view(['GET'])
def getdaos(request):
    daos = Daos.objects.all()
    serializer = DaosSerializer(daos, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def gettest(request):
    daos = Daos.objects.all()
    serializer = DaosSerializer(daos, many=True)
    return Response("serializer.data", status=status.HTTP_200_OK)

@api_view(['POST'])
def setdaos(request):
    # profileImage = ProfileImageDicty.objects.create(
    #     profileImageHash = request.data['profileImage'].get('hash'),
    #     profileImageUrl = request.data['profileImage'].get('url')
    # )
    dao = Daos.objects.create(
        daoName = request.data['daoProfile'].get('daoName'),
        profileImage = request.data['daoProfile'].get('profileImage'),
        categories = request.data['daoProfile'].get('categories'),
        description = request.data['daoProfile'].get('description'),
        keyPermissions = request.data.get('keyPermissions'),
        vaultDetails = request.data.get('vaultDetails'),
        votingParameters = request.data.get('votingParameters'),
    )
    serializer = DaosSerializer(dao, many = False)
    # if serializer.is_valid():
    #     serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)

    # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)