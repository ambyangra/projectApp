# Generated by Django 5.0.6 on 2024-07-08 06:30

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0011_tournament_current_round"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tournament",
            name="current_round",
            field=models.PositiveIntegerField(default=1),
        ),
    ]