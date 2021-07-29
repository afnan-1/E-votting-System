from votingsystem.serializers import SocietyCandidateSerializer, SocietyIdsSerializer, SocietySerializer
from votingsystem.models import Societie, SocietyCandidate, StudentUserName
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.
@api_view(["GET",])
def get_all_societies(request):
    society = Societie.objects.all()
    serializer = SocietyIdsSerializer(society,many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_society(request,id):
    society = Societie.objects.get(id=id)
    serializer = SocietySerializer(society,many=False)
    return Response(serializer.data)


@api_view(['POST'])
def add_vote(request):
    data = request.data
    candidate = SocietyCandidate.objects.get(id=data['candidate_id'])
    voter_list = StudentUserName.objects.all()
    for i in voter_list:
        if i.username == request.user.username:
            if i.candidate.member_name == candidate.member_name:
                return Response("You Vote already")
    candidate.votes += 1
    candidate.save()
    voter = StudentUserName()
    voter.username = request.user.username
    voter.candidate = candidate
    voter.save()

    # result = Result()
    # result.soc_candidate = candidate
    # result.result += 1
    return Response("vote added",status=200)
    

@api_view()
def get_result(request):
    candidates = Societie.objects.all()
    serializer = SocietySerializer(candidates,many=True)
    return Response(serializer.data)

