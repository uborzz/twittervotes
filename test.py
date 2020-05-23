from core import read_config
from twitter_auth import get_oauth_token

from core.twitter import Hashtag, HashtagStatsManager
from core import execute_request
from pprint import pprint


def test_read_config_get_token():
    c = read_config()
    get_oauth_token(c)


def test_stats_manager():
    hashtag = Hashtag("python")
    stats = HashtagStatsManager((hashtag.name,))
    data = execute_request(hashtag)
    stats.update(data)

    print("stats")
    for (_, item) in stats.hashtags.items():
        print(vars(item))


if __name__ == "__main__":

    # test_read_config_get_token()
    test_stats_manager()
