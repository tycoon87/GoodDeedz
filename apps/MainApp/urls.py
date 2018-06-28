from django.conf.urls import url
from . import views

urlpatterns = [
url(r'^$', views.index),
url(r'^createUser$', views.createUser),
url(r'^Add$', views.Add),
url(r'^Login$' , views.Login),
url(r'^Logout$', views.Logout),
url(r'^FriendPage$', views.FriendPage),
url(r'^AddFriend/(?P<User_id>\d+)$' , views.AddFriend),
url(r'^UnFriend/(?P<User_id>\d+)$' , views.UnFriend),
]