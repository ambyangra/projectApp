from rest_framework import serializers
from django.contrib.auth.models import AnonymousUser
from .models import Player, Team, Coach, User, Game, Tournament, LeagueAdmin

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ['id', 'name', 'average_score', 'games_participated', 'team']

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['id', 'team_name', 'team_size', 'league_admin', 'is_eliminated', 'tournament']

class CoachSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coach
        fields = ['id', 'name', 'team']

class LeagueAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeagueAdmin
        fields = ['id', 'name']        

class UserSerializer(serializers.ModelSerializer):
    is_coach = serializers.SerializerMethodField()
    is_player = serializers.SerializerMethodField()
    is_league_admin = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'username', 'user_type', 'is_coach', 'is_player', 'is_league_admin']

    def get_is_coach(self, obj):
        return getattr(obj, 'user_type', '') == 'coach'

    def get_is_player(self, obj):
        return getattr(obj, 'user_type', '') == 'player'

    def get_is_league_admin(self, obj):
        return getattr(obj, 'user_type', '') == 'league_admin'


class GameSerializer(serializers.ModelSerializer):
    team_a = TeamSerializer()
    team_b = TeamSerializer()

    class Meta:
        model = Game
        fields = ['id', 'team_a', 'team_b', 'score_a', 'score_b', 'date']

class TournamentSerializer(serializers.ModelSerializer):
    winning_team = TeamSerializer(read_only=True)

    class Meta:
        model = Tournament
        fields = ['id', 'name', 'start_date', 'end_date', 'winning_team', 'current_round']
