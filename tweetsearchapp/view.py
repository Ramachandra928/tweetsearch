# python built-in imports
import twitter

# django built-in imports
from django.shortcuts import render
from django.views.generic import View
from django.template import RequestContext, loader
from django.http import HttpResponseRedirect, HttpResponse

# application imports
from tweetsearchapp.models import update_search_model
from tweetsearchapp.api import get_access_token, search
from tweetsearch.settings import TWITTER_OAUTH_KEY, TWITTER_OAUTH_SECRET


class TweetSearch(View):
    def get(self, request):
        """
        This method renders tweet search page

        @return : tweet search html page
        """
        return render(request, 'tweet_search/search_tweets.html', dict())


class TweetSearchResults(View):
    def get(self, request):
        """
        This method reads phrase from request and updates model.
        Also searches tweets matching from twitter api

        @return : returns tweet search results template 
        """
        tweet_phrase = request.GET.get('tweet_phrase')
        if not tweet_phrase:
            return render(request, 'tweet_search/validation.html', dict())
        num_times_searched, last_time_used = update_search_model(tweet_phrase)
        access_token = get_access_token(TWITTER_OAUTH_KEY, TWITTER_OAUTH_SECRET)
        resultset = search(tweet_phrase, access_token)
        template_params = {'resultset': resultset,
                           'tweet_phrase': tweet_phrase,
                           'num_times_searched': num_times_searched,
                           'last_time_used': last_time_used}
        return render(request, 'tweet_search/tweet_results.html', template_params)

