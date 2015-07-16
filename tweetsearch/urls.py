from django.conf.urls import patterns, url, include

urlpatterns = patterns('',
	url(r'^tweetsearch/', include('tweetsearchapp.urls', namespace="tweetsearchapp")),
)
