#pip install requests_oauthlib
#pip install pytest
import pytest
import os
from requests_oauthlib import OAuth1Session

consumer_key = os.environ.get('CONSUMER_KEY')
consumer_key = os.environ.get('CONSUMER_SECRET')
access_token_key = os.environ.get('ACCESS_TOKEN_KEY')
access_token_secret = os.environ.get('ACCESS_TOKEN_SECRET')

def test_login_to_twitter():
    url = 'https://api.twitter.com/1.1/account/verify_credentials.json'
    twitter = OAuth1Session(consumer_key, consumer_key, access_token_key, access_token_secret)
    r = twitter.get(url)
    assert r.status_code == 200
