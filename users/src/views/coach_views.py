from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import Player, Coach
from ..serializers import TeamSerializer, PlayerSerializer, CoachSerializer

class CoachView(APIView):
    def get(self, request):
        user = request.user
        try:
            coach = Coach.objects.get(name=user.username)
            team = coach.team
            team_serializer = TeamSerializer(team)

            players = Player.objects.filter(team=team)
            player_serializer = PlayerSerializer(players, many=True)

            return Response({
                'team': team_serializer.data,
                'players': player_serializer.data
            })
        except Coach.DoesNotExist:
            return Response({'Error': 'Coach not found'}, status=404)

    def put(self, request):
        try:
            coach = Coach.objects.get(user=request.user)
            coach_serializer = CoachSerializer(coach, data=request.data, partial=True)
            if coach_serializer.is_valid():
                coach_serializer.save()
                return Response(coach_serializer.data)
            return Response(coach_serializer.errors, status=400)
        except Coach.DoesNotExist:
            return Response({'Error': 'Coach not found'}, status=404)

class CreateCoachView(APIView):
    def post(self, request):
        serializer = CoachSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
