# python built-in imports
import base64
import requests

# application imports
from tweetsearch.settings import OAUTH_URL, TWEET_URL


def get_access_token(key, secret):
    """
    This method gets access token using key and secret.
    """

    # define headers and params
    content_type = "application/x-www-form-urlencoded;charset=UTF-8"
    key_secret = "{}:{}".format(key, secret)
    authorisation = "Basic {}".format(base64.urlsafe_b64encode(key_secret))

    headers = {'Content-Type': content_type,
               'Authorization': authorisation}
    params = {'grant_type': "client_credentials"}

    # calling twitter api
    response = requests.post(OAUTH_URL, params=params, headers=headers).json()

    if 'errors' in response:
        raise_exception(response['errors'])
    if response['token_type'] != "bearer":
        raise TwitterAPI.TwitterAPIException(
            "Oauth returned with no bearer access token")
    
    return response['access_token']


def search(tweet_phrase, access_token):
    """
    This method searches tweets matching phase
    """
    headers = {'Authorization': "Bearer " + access_token}
    params = {'q': tweet_phrase}

    response = requests.get(TWEET_URL, params=params, headers=headers).json()

    if 'errors' in response:
        raise_exception(response['errors'])
    return response['statuses']
	
def raise_exception(*errors):
  """
	This method raise exception when phrase is not passed
	"""
    error_string = ""
    for error in errors[0]:
        if 'message' in error:
            error_string = error_string + error['message']

    raise APIException(error_string)
	
class APIException(Exception):
    """
		Exception class
		"""
        def __init__(self, value):
            self.value = value
        def __str__(self):
            return repr(self.value)
