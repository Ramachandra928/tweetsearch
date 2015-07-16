# python built-in imports
import datetime

# django built-in imports
from django.db import models



class TweetPhrase(models.Model):
    text = models.CharField(max_length=100)
    num_times_searched = models.IntegerField(default=0)
    last_search_datetime = models.DateTimeField('last searched', auto_now=True)
	
def update_search_model(tweet_phrase):
    """
    Updates number of times searched using phrase and last time of search.

    @return : returns 	
    """
    model, created = TweetPhrase.objects.get_or_create(
        text=tweet_phrase, defaults={'num_times_searched': 1})
    last_time_used = datetime.datetime.now()
    if not created:
        last_time_searched = model.last_search_datetime
        model.num_times_searched += 1
        model.last_search_datetime = datetime.datetime.now()
        model.save()

    return (model.num_times_searched, last_time_used)
