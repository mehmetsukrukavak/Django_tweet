from django.shortcuts import render

# Create your views here.
def list_tweet(request):
    return render(request,'tweetapp/listtweet.html')


def add_tweet(request):
    return render(request,'tweetapp/addtweet.html')
