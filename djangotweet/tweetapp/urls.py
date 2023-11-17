from django.urls import path
from . import views


app_name = "tweetapp"


urlpatterns = [
    path("", views.list_tweet, name="listtweet"),
    path("addtweet/", views.add_tweet, name="addtweet")
]