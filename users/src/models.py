from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    USER_TYPES = (
        ('coach', 'Coach'),
        ('player', 'Player'),
        ('league_admin', 'League Admin'),
    )
    user_type = models.CharField(max_length=20, choices=USER_TYPES, default='player')
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='users',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='users',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )

class Player(models.Model):
    name = models.CharField("Player Name", max_length=240)
    average_score = models.IntegerField("Average Score", default=0)
    games_participated = models.IntegerField("Number of Games Played", default=0)
    team = models.ForeignKey("Team", on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.name

class Coach(models.Model):
   name = models.CharField("Coach Name", max_length=240)
   team = models.OneToOneField("Team", on_delete=models.CASCADE, null=True, blank=True, related_name="coach" )
   def __str__(self):
        return self.name

class Team(models.Model):
    team_name = models.CharField("Team name", max_length=240)
    team_size = models.PositiveIntegerField("Team Size", default=10)
    league_admin = models.ForeignKey("LeagueAdmin", on_delete=models.SET_NULL, null=True, blank=True)
    is_eliminated = models.BooleanField(default=False)
    tournament = models.ForeignKey("Tournament", on_delete=models.CASCADE, null=True, blank=True, related_name="teams")
    def __str__(self):
        return self.team_name
    def get_team_size(self):
        return self.team_size

class LeagueAdmin(models.Model):
    name = models.CharField("League Admin Name", max_length=240)
    def __str__(self):
        return self.name

class Game(models.Model):
    team_a = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team_a')
    team_b = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team_b')
    score_a = models.IntegerField()
    score_b = models.IntegerField()
    date = models.DateTimeField()
    tournament = models.ForeignKey('Tournament', on_delete=models.CASCADE, related_name='games')
    def __str__(self):
        return f"{self.team_a.team_name} vs {self.team_b.team_name}"
    
class Tournament(models.Model):
    name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    current_round = models.PositiveIntegerField(default=1)
    winning_team = models.ForeignKey('Team', on_delete=models.SET_NULL, null=True, related_name='tournament_winners')
    def __str__(self):
        return self.name    