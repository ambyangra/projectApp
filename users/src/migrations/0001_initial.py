# Generated by Django 5.0.6 on 2024-07-07 07:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Coach",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=240, verbose_name="Coach Name")),
            ],
        ),
        migrations.CreateModel(
            name="LeagueAdmin",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(max_length=240, verbose_name="League Admin Name"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Team",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "team_name",
                    models.CharField(max_length=240, verbose_name="Team name"),
                ),
                (
                    "coach",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING, to="users.coach"
                    ),
                ),
                (
                    "league_admin",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="users.leagueadmin",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Player",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=240, verbose_name="Player Name")),
                ("average_score", models.IntegerField(verbose_name="Average Score")),
                (
                    "num_games",
                    models.IntegerField(verbose_name="Number of Games Played"),
                ),
                (
                    "team",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="users.team",
                    ),
                ),
            ],
        ),
    ]
