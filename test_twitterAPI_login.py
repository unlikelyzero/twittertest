#pip install requests_oauthlib
#pip install pytest
import pytest
from requests_oauthlib import OAuth1Session

def test_login_to_twitter():
    url = 'https://api.twitter.com/1.1/account/verify_credentials.json'
    twitter = OAuth1Session(consumer_key, consumer_secret, access_token_key, access_token_secret)
    r = twitter.get(url)
    assert r.status_code == 200
