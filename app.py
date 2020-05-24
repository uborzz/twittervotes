from core import parse_commandline_args, execute_request, Runner
from core.twitter import HashtagStatsManager, Hashtag

from core.app_logger import get_logger

from time import sleep


class Application:
    def __init__(self, hashtags):
        self._manager = HashtagStatsManager(hashtags)
        self._runner = Runner(self._on_success, self._on_error, self._on_complete)
        self._logger = get_logger()

    def fetch_data(self):
        self._runner.exec(execute_request, self._manager.hashtags)

    def output(self):
        for (_, hashtag) in self._manager.hashtags.items():
            self._logger.info(f"Results for {hashtag.name}: {hashtag.total}")

    def _on_error(self, error_message):
        raise Exception(error_message)

    def _on_success(self, data):
        self._manager.update(data)

    def _on_complete(self):
        ...


def main():
    args = parse_commandline_args()
    app = Application(args.hashtags)

    # TODO App gui

    # Test
    print("First fetch")
    app.fetch_data()
    app.output()

    sleep(3)
    print("Showing results after 3 seconds...")
    app.fetch_data()
    app.output()

    sleep(3)
    print("Showing results 3 seconds later...")
    app.fetch_data()
    app.output()


if __name__ == "__main__":
    main()
