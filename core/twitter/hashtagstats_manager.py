from .hashtag import Hashtag

from typing import Sequence


class HashtagStatsManager:
    def __init__(self, hashtags: Sequence[str]):
        if not hashtags:
            raise AttributeError("hashtags must be provided")
        self._hashtags = {hashtag: Hashtag(hashtag) for hashtag in hashtags}
        print("_hashtags:", self._hashtags)

    def update(self, data):
        hashtag, results = data
        metadata = results.get("search_metadata")
        refresh_url = metadata.get("refresh_url")
        statuses = results.get("statuses")

        total = len(statuses)

        if total > 0:
            self._hashtags.get(hashtag.name).total += total
            self._hashtags.get(hashtag.name).refresh_url = refresh_url

    @property
    def hashtags(self):
        return self._hashtags
