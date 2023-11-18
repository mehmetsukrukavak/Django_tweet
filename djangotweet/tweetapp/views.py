from django.shortcuts import render, redirect
from . import models
from django.urls import reverse
#from . import forms
from tweetapp.forms import AddTweetForm, AddTweetModelForm

# Create your views here.
def list_tweet(request):
    all_tweets = models.Tweet.objects.all()
    tweet_dict = { "tweets": all_tweets}
    return render(request,'tweetapp/listtweet.html', context=tweet_dict)


def add_tweet(request):
    if request.POST:
        nickname = request.POST["nickname"]
        message = request.POST["message"]
        models.Tweet.objects.create(nickname=nickname, message=message)
        return redirect(reverse('tweetapp:listtweet'))
    else:
        return render(request,'tweetapp/addtweet.html')
    

def add_tweet_by_form(request):
      if request.POST:
          form = AddTweetForm(request.POST)
          if form.is_valid():
            nickname = form.cleaned_data["nickname_input"]
            message = form.cleaned_data["message_input"]
            models.Tweet.objects.create(nickname=nickname, message=message)
            return redirect(reverse('tweetapp:listtweet'))
          else:
            print("error in form")
            return render(request,'tweetapp/addtweetbyform.html', context={"form":form})
          
      else:
        form = AddTweetForm()
        return render(request,'tweetapp/addtweetbyform.html', context={"form":form})
      

def add_tweet_by_modelform(request):
      if request.POST:
          form = AddTweetModelForm(request.POST)
          if form.is_valid():
            nickname = form.cleaned_data["nickname"]
            message = form.cleaned_data["message"]
            models.Tweet.objects.create(nickname=nickname, message=message)
            return redirect(reverse('tweetapp:listtweet'))
          else:
            print("error in form")
            return render(request,'tweetapp/addtweetbymodelform.html', context={"form":form})
          
      else:
        form = AddTweetModelForm()
        return render(request,'tweetapp/addtweetbymodelform.html', context={"form":form})