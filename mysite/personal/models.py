from django.db import models
from django.contrib.auth.models import User

"""
	Helpful functions
	find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
	find . -path "*/migrations/*.pyc"  -delete
	python3 manage.py makemigrations
	python3 manage.py migrate
"""

# class Availability(models.Model):
# 	AVAILABILITY_TYPE = (
# 		('p','person'),
# 		('c','court'),
# 		('t','team'),
# 	)
# 	availability_type = models.CharField(max_length=1, choices=AVAILABILITY_TYPE)
# 	object_link_id = models.PositiveIntegerField(default = 0)

# class Day(Availability):
#     tuesday = models.PositiveIntegerField(default = 0)
#     wednesday = models.PositiveIntegerField(default = 0)
#     thursday = models.PositiveIntegerField(default = 0)
#     friday = models.PositiveIntegerField(default = 0)
#     saturday = models.PositiveIntegerField(default = 0)
#     sunday = models.PositiveIntegerField(default = 0)

# class Hour(Day):
# 	hourDay = models.PositiveIntegerField(default = 0)

# class Minute(Hour):
# 	minteHour = models.PositiveIntegerField(default = 0)
class Team(models.Model):
	player1 = models.ForeignKey(User, related_name = 'player1', on_delete=models.CASCADE)
	player2 = models.ForeignKey(User, related_name = 'player2', on_delete=models.CASCADE)
	total_wins = models.PositiveIntegerField(default = 0)
	leaderboard_position = models.PositiveIntegerField(default = 1)

class Court(models.Model):
	name = models.CharField(max_length = 100)
	address = models.CharField(max_length = 100)

class Game(models.Model):
	date = models.DateTimeField()
	week = models.PositiveIntegerField(default = 1)
	has_been_played = models.BooleanField(default=False)
	team1 = models.ForeignKey(Team, related_name = 'team1', on_delete=models.CASCADE)
	team2 = models.ForeignKey(Team, related_name = 'team2', on_delete=models.CASCADE)
	winning_team = models.ForeignKey(Team, related_name = 'winning_team', blank=True, null=True, on_delete=models.CASCADE)
	court = models.ForeignKey(Court, related_name = 'court', on_delete=models.CASCADE)

class Player(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	team = models.ForeignKey(Team, blank=True, null=True, on_delete=models.SET_NULL)

class Availability(models.Model):
	player = models.ForeignKey(User, on_delete=models.CASCADE)
	availability = models.DateTimeField(blank=True, null=True)

class Booking(models.Model):
	court = models.ForeignKey(Court, on_delete=models.CASCADE)
	game = models.ForeignKey(Game, on_delete=models.CASCADE)
	start = models.DateTimeField()
	end = models.DateTimeField()










