from django.test import TestCase


class tweetSearchTest(TestCase):

    def test_tweet_search_page(self):
        response = self.client.get("http://127.0.0.1:8000/tweetsearch")
        self.assertEqual(response.status_code, 301)

    def test_tweet_search_results(self):
        response = self.client.get(
            "http://127.0.0.1:8000/tweetsearch/search/?csrfmiddlewaretoken=Q4qILIRafr5NCAkmr0zkBpaZbTz5OX2k&tweet_phrase=test")
        self.assertContains(response, '<li>', status_code=200)
        self.assertTemplateUsed(response, 'tweet_search/tweet_results.html')

    def test_api_search(self):
        from views import search
        access_token = u'AAAAAAAAAAAAAAAAAAAAAEtYdwAAAAAAmsMTQS0s7IMdYRKSxLenW%2BR2%2Fq4%3DbjQjzkdJD6ESKHMMXkTRMlhXlXqu3zpW0HRFNwadoVyE0tqn9l'
        search_result = search('test', access_token)
        self.assertEqual(len(search_result), 15)

    def test_api_search_failure(self):
        from api import APIException
        from views import search
        search_result = lambda : search('test', 'Wrong access token')
        self.assertRaises(APIException, search_result)

    def test_access_token(self):
        from views import get_access_token
        from tweetsearch.settings import TWITTER_OAUTH_KEY, TWITTER_OAUTH_SECRET
        access_token = get_access_token(TWITTER_OAUTH_KEY, TWITTER_OAUTH_SECRET)
        expected_access_token = u'AAAAAAAAAAAAAAAAAAAAAEtYdwAAAAAAmsMTQS0s7IMdYRKSxLenW%2BR2%2Fq4%3DbjQjzkdJD6ESKHMMXkTRMlhXlXqu3zpW0HRFNwadoVyE0tqn9l'
        self.assertEqual(access_token, expected_access_token)
		
    def test_access_token_failure(self):
        from api import APIException
        from views import get_access_token
        access_token = lambda : get_access_token('Wrong Key', 'Wrong Secret')
        self.assertRaises(APIException, access_token)
