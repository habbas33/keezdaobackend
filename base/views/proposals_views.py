from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from base.models.proposals_models import *
from base.serializers.proposals_serializer import *


@api_view(['GET'])
def getallproposals(request):
    proposals = Proposal.objects.all()
    serializer = ProposalsSerializer(proposals, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def getproposalbyname(request):
    info=request.query_params.get("info")
    if info != None:
        proposal= Proposal.objects.filter(proposalName__icontains=info)
        serializer = ProposalsSerializer(proposal, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        serializer = ProposalsSerializer([], many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def getproposalbytype(request):
    info=request.query_params.get("info")
    if info != None:
        proposal= Proposal.objects.filter(proposalType__icontains=info)
        serializer = ProposalsSerializer(proposal, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        serializer = ProposalsSerializer([], many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def getproposalbycid(request):
    info=request.query_params.get("info")
    if info != None:
        proposal= Proposal.objects.get(CID=info)
        serializer = ProposalsSerializer(proposal, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        serializer = ProposalsSerializer([], many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def getproposalbyidentifier(request):
    info=request.query_params.get("info")
    if info != None:
        proposal= Proposal.objects.get(identifier=info)
        serializer = ProposalsSerializer(proposal, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        serializer = ProposalsSerializer([], many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def getproposalbycreator(request):
    info=request.query_params.get("info")
    if info != None:
        proposal= Proposal.objects.filter(creator__icontains=info)
        serializer = ProposalsSerializer(proposal, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        serializer = ProposalsSerializer([], many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def getproposalbycategory(request):
    info=request.query_params.get("info")
    if info != None:
        proposal = Proposal.objects.filter(categories__icontains=info)
        # print('query',proposal);
        serializer = ProposalsSerializer(proposal, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        serializer = ProposalsSerializer([], many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def getproposalbydaocid(request):
    info=request.query_params.get("info")
    if info != None:
        proposal = Proposal.objects.filter(forDaoDetails__icontains=info)
        serializer = ProposalsSerializer(proposal, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        serializer = ProposalsSerializer([], many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def getproposalbydaoname(request):
    info=request.query_params.get("info")
    if info != None:
        proposal = Proposal.objects.filter(forDaoDetails__icontains=info)
        serializer = ProposalsSerializer(proposal, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        serializer = ProposalsSerializer([], many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def setproposals(request):
    daproposal = Proposal.objects.create(
        proposalType = request.data['proposalProfile'].get('proposalType'),
        proposalName = request.data['proposalProfile'].get('proposalName'),
        categories = request.data['proposalProfile'].get('categories'),
        description = request.data['proposalProfile'].get('description'),

        proposalDetails = request.data.get('proposalDetails'),
        forDaoDetails = request.data.get('forDaoDetails'),
        url = request.data['proposalProfile'].get('url'),
        CID = request.data['proposalProfile'].get('CID'),
        identifier = request.data['proposalProfile'].get('identifier'),
        creator = request.data['proposalProfile'].get('creator'),
        createdAt = request.data.get('createdAt'),
    )
    serializer = ProposalsSerializer(daproposal, many = False)
    return Response(serializer.data, status=status.HTTP_201_CREATED)