from django.conf.urls import patterns, url

from tweetsearchapp.views import TweetSearch, TweetSearchResults

urlpatterns = patterns('',
	url(r'^$', TweetSearch.as_view(), name='search_tweets'),
	url(r'^search/$', TweetSearchResults.as_view(), name='search_results'),
)
