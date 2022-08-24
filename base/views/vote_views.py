from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from base.models.vote_models import *
from base.serializers.vote_serializer import *


@api_view(['GET'])
def getallvotes(request):
    vote = Vote.objects.all()
    serializer = VotesSerializer(vote, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def getvotesbyproposalsignature(request):
    info=request.query_params.get("info")
    if info != None:
        vote= Vote.objects.filter(proposalSignature__icontains=info)
        serializer = VotesSerializer(vote, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        serializer = VotesSerializer([], many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def getvotesbyproposalurl(request):
    info=request.query_params.get("info")
    if info != None:
        vote= Vote.objects.filter(proposalUrl__icontains=info)
        serializer = VotesSerializer(vote, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        serializer = VotesSerializer([], many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

# @api_view(['GET'])
# def getvotesbyproposalcid(request):
#     info=request.query_params.get("info")
#     if info != None:
#         vote= Vote.objects.filter(proposalName__icontains=info)
#         serializer = VotesSerializer(vote, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     else:
#         serializer = VotesSerializer([], many=True)
#     return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def getvotesbyvoter(request):
    info=request.query_params.get("info")
    if info != None:
        vote= Vote.objects.filter(VoterAddress__icontains=info)
        serializer = VotesSerializer(vote, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        serializer = VotesSerializer([], many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def setvote(request):
    userVote = Vote.objects.create(
        proposalContractAddress = request.data.get('proposalContractAddress'),
        proposalName = request.data.get('proposalName'),
        proposalUrl = request.data.get('proposalUrl'),
        proposalSignature = request.data.get('proposalSignature'),
        VoterSignature = request.data.get('VoterSignature'),
        VoterChoice = request.data.get('VoterChoice'),
        VoterAddress = request.data.get('VoterAddress'),
        createdAt = request.data.get('createdAt'),
    )
    serializer = VotesSerializer(userVote, many = False)
    return Response(serializer.data, status=status.HTTP_201_CREATED)

