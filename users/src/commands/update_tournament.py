from django.core.management.base import BaseCommand
from ..models import Tournament, Game, Team, Player
from ..views import PlayerView
from rest_framework.response import Response
from rest_framework.request import Request
import random

class Command(BaseCommand):
    help = 'Update the tournament progress and game results'

    def handle(self, *args, **options):
        # Retrieve the current tournament
        tournament = Tournament.objects.latest('id')

        # Check the current round and update the tournament progress
        self.update_tournament_progress(tournament)

        # Update the game results for the current round
        self.update_game_results(tournament)

        self.stdout.write(self.style.SUCCESS('Tournament progress and game results updated successfully.'))

    def update_tournament_progress(self, tournament):
        # Get the teams in the current round
        current_teams = Team.objects.filter(tournament=tournament, is_eliminated=False)

        # Check if the current round is the final round
        if len(current_teams) == 1:
            # Set the winning team
            tournament.winning_team = current_teams.first()
            tournament.current_round = tournament.FINAL_ROUND
            tournament.save()
            return

        # Move teams to the next round
        next_round_teams = []
        for i in range(0, len(current_teams), 2):
            team_a = current_teams[i]
            team_b = current_teams[i + 1]
            winner = self.determine_game_winner(team_a, team_b)
            next_round_teams.append(winner)

        # Update the teams for the next round
        for team in next_round_teams:
            team.is_eliminated = False
            team.save()

        for team in current_teams:
            if team not in next_round_teams:
                team.is_eliminated = True
                team.save()

        # Update the tournament's current round
        tournament.current_round += 1
        tournament.save()        

    def update_game_results(self, tournament):
        current_games = Game.objects.filter(tournament=tournament, is_completed=False)
        for game in current_games:
            team_a_score, team_b_score = self.simulate_game(game.team_a, game.team_b)
            game.score_a = team_a_score
            game.score_b = team_b_score
            game.is_completed = True
            game.save()

            self.update_player_stats(game.team_a, team_a_score)
            self.update_player_stats(game.team_b, team_b_score)

    def determine_game_winner(self, team_a, team_b):
        team_a_score = self.simulate_game(team_a, team_b)[0]
        team_b_score = self.simulate_game(team_a, team_b)[1]
        if team_a_score > team_b_score:
            return team_a
        else:
            return team_b

    def simulate_game(self, team_a, team_b):
        team_a_score = random.randint(60, 100)
        team_b_score = random.randint(60, 100)
        return team_a_score, team_b_score

    def update_player_stats(self, team, score):
        players = Player.objects.filter(team=team)
        for player in players:
            request = Request(data={
                'average_score': player.average_score + (score / len(players)),
                'games_participated': player.games_participated + 1
            })
            view = PlayerView()
            view.put(request, player.pk)