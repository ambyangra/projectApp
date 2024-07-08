from django.urls import path
from .views.league_admin_views import LeagueAdminView, CreateLeagueAdminView
from .views.coach_views import CoachView, CreateCoachView
from .views.player_views import PlayerView, CreatePlayerView
from .views.user_views import UserDetailView
from .views.tournament_views import TournamentListView, TournamentDetailView, ScoreboardView

urlpatterns = [
    path('league-admin/', LeagueAdminView.as_view(), name='league-admin'),
    path('league-admin/create/', CreateLeagueAdminView.as_view(), name='create-league-admin'),
    path('coaches/', CoachView.as_view(), name='coach'),
    path('coaches/<int:pk>/', CoachView.as_view(), name='coach-detail'),
    path('coaches/create/', CreateCoachView.as_view(), name='coach-create'),
    path('players/', PlayerView.as_view(), name='player'),
    path('players/create/', CreatePlayerView.as_view(), name='player-create'),
    path('users/', UserDetailView.as_view(), name='user'),
    path('tournaments/', TournamentListView.as_view(), name='tournament-list'),
    path('tournaments/<int:pk>/', TournamentDetailView.as_view(), name='tournament-detail'),
    path('scoreboard/', ScoreboardView.as_view(), name='scoreboard'),
]