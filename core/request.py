import oauth2 as oauth
import time
from urllib.parse import parse_qsl
import json

import requests

from .config import read_config, read_reqauth

from .twitter import Hashtag


def prepare_request(url, url_params):
    reqconfig = read_reqauth()
    config = read_config()

    token = oauth.Token(key=reqconfig.oauth_token, secret=reqconfig.oauth_token_secret)

    consumer = oauth.Consumer(key=config.consumer_key, secret=config.consumer_secret)

    params = {
        "oauth_version": "1.0",
        "oauth_nonce": oauth.generate_nonce(),
        "oauth_timestamp": str(int(time.time())),
        "oauth_token": token.key,
        "oauth_consumer_key": consumer.key,
    }

    params.update(url_params)

    req = oauth.Request(method="GET", url=url, parameters=params)

    signature_method = oauth.SignatureMethod_HMAC_SHA1()
    req.sign_request(signature_method, consumer, token)
    return req.to_url()


def execute_request(hashtag: Hashtag):
    config = read_config()

    if hashtag.refresh_url:
        refresh_url = hashtag.refresh_url[1:]
        url_params = dict(parse_qsl(refresh_url))
    else:
        url_params = {"q": f"#{hashtag.name}", "result_type": "mixed"}

    url = prepare_request(config.search_endpoint, url_params)

    data = requests.get(url)

    results = json.loads(data.text)

    return (
        hashtag,
        results,
    )
