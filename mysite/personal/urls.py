from django.conf.urls import url, include
from . import views, models, db
from django.views.generic import ListView, DetailView
from django.contrib.auth import views as auth_views

urlpatterns = [
	url(r'^$', views.index, name='home'),
	#url(r'^$', ListView.as_view(queryset=db.Sqlcommand.get_teamTable_gameTable(), template_name="personal/homeL.html")),
	url(r'^profile/$', views.profile, name='profile'),
	url(r'^manageGames/$', views.manageGames, name='manage games'),
	url(r'^accountSettings/$', views.accountSettings, name='manage games'),
	url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
	]

