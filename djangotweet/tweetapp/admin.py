from django.contrib import admin
#from . import models
from tweetapp.models import Tweet

# Register your models here.
class TweetAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Nickname Group",{"fields":["nickname"]}),
        ("Message Group",{"fields":["message"]})
    ]
   #fields =['message','nickname']


admin.site.register(Tweet, TweetAdmin)
