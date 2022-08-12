from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from base.models.daos_models import *
from base.serializers.daos_serializer import *


@api_view(['GET'])
def getalldaos(request):
    daos = Daos.objects.all()
    serializer = DaosSerializer(daos, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def getdaobyname(request):
    info=request.query_params.get("info")
    if info != None:
        dao= Daos.objects.filter(daoName__icontains=info)
        serializer = DaosSerializer(dao, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        serializer = DaosSerializer([], many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def getdaobycid(request):
    info=request.query_params.get("info")
    if info != None:
        dao= Daos.objects.get(CID=info)
        serializer = DaosSerializer(dao, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        serializer = DaosSerializer([], many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def getdaobyup(request):
    info=request.query_params.get("info")
    if info != None:
        dao= Daos.objects.get(daoUpAddress=info)
        serializer = DaosSerializer(dao, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        serializer = DaosSerializer([], many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def getdaobycreator(request):
    info=request.query_params.get("info")
    if info != None:
        dao= Daos.objects.filter(creator__icontains=info)
        serializer = DaosSerializer(dao, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        serializer = DaosSerializer([], many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def getdaosbycategory(request):
    info=request.query_params.get("info")
    if info != None:
        daos = Daos.objects.filter(categories__icontains=info)
        print('query',daos);
        serializer = DaosSerializer(daos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        serializer = DaosSerializer([], many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def getdaosbymember(request):
    info=request.query_params.get("info")
    if info != None:
        daos = Daos.objects.filter(keyPermissions__icontains=info)
        print('query',daos);
        serializer = DaosSerializer(daos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        serializer = DaosSerializer([], many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def setdaos(request):
    dao = Daos.objects.create(
        daoName = request.data['daoProfile'].get('daoName'),
        profileImage = request.data['daoProfile'].get('profileImage'),
        categories = request.data['daoProfile'].get('categories'),
        description = request.data['daoProfile'].get('description'),
        keyPermissions = request.data.get('keyPermissions'),
        vaultDetails = request.data.get('vaultDetails'),
        votingParameters = request.data.get('votingParameters'),
        url = request.data['daoProfile'].get('url'),
        CID = request.data['daoProfile'].get('CID'),
        daoUpAddress = request.data['daoProfile'].get('daoUpAddress'),
        creator = request.data['daoProfile'].get('creator'),
        createdAt = request.data.get('createdAt'),
    )
    serializer = DaosSerializer(dao, many = False)
    return Response(serializer.data, status=status.HTTP_201_CREATED)