from django.urls import path
from . import views


app_name = "tweetapp"


urlpatterns = [
    path("", views.list_tweet, name="listtweet"),
    path("addtweet/", views.add_tweet, name="addtweet"),
    path("addtweetbyform/", views.add_tweet_by_form, name="addtweetbyform"),
    path("addtweetbymodelform/", views.add_tweet_by_modelform, name="addtweetbymodelform"),
    path("signup/",views.SignUpView.as_view(), name="signup"),
    path("deletetweet/<int:id>", views.delete_tweet, name="deletetweet")
]