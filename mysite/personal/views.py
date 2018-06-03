from django.shortcuts import render
from . import models, db

def index(request):
	team = db.Sql.get_teamTable()
	game = db.Sql.get_gameTable(request)

	return render(request, 'personal/homeL.html', {'content': [team, game]})

def profile(request):
	return render(request, 'personal/profile.html')

def manageGames(request):
	games_played = db.Sql.get_games_where_player_involved_have_been_played(request)
	count = db.Sql.get_not_played_games(request)
	game_to_be_played = db.Sql.get_games_where_player_involved_not_been_played(request)
	current_date = db.Other.get_date_time()
	
	""" 
	If the is only one game that hasn't been played
	Further analysis is required to determine the correct section
	Compare date to the current date
	If greater than current -> upcoming game
	Else it is a latest match 
	"""
	if(len(game_to_be_played) == 1):
		if(current_date < game_to_be_played[0].date):
			is_upcoming = True
		else:
			is_upcoming = False
	else:
		is_upcoming = None

	return render(request, 'personal/manageGames.html', {'content': [games_played, count, game_to_be_played, is_upcoming]})

def accountSettings(request):
	return render(request, 'personal/accountSettings.html',{'content': [0,1,2,3]})
