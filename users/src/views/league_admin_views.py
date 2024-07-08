from rest_framework.views import APIView
from rest_framework.response import Response
from ..models import Team, Player
from rest_framework import status
from ..serializers import TeamSerializer, PlayerSerializer, LeagueAdminSerializer

class LeagueAdminView(APIView):
    def get(self, request):
        teams = Team.objects.all()
        team_serializer = TeamSerializer(teams, many=True)

        players = Player.objects.all()
        player_serializer = PlayerSerializer(players, many=True)

        return Response({
            'teams': team_serializer.data,
            'players': player_serializer.data
        })

class CreateLeagueAdminView(APIView):
    def post(self, request):
        serializer = LeagueAdminSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
