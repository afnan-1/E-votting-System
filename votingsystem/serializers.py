from rest_framework import serializers
from .models import Societie,SocietyCandidate


class SocietyCandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocietyCandidate
        fields = "__all__"

class SocietySerializer(serializers.ModelSerializer):
    candidate = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Societie
        fields = '__all__'
    def get_candidate(self,obj):
        candidate = obj.society.all()
        serializer = SocietyCandidateSerializer(candidate,many=True)
        return serializer.data


class SocietyIdsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Societie
        fields = ['id',]

