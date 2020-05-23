from argparse import ArgumentParser

from .app_logger import get_logger


def validated_args(args):
    logger = get_logger()

    hashtags = args.hashtags
    unique_hashtags = list(set(args.hashtags))

    if len(unique_hashtags) < len(hashtags):
        logger.info(("Ignoring some hashtags (duplicated)."))
        hashtags = unique_hashtags

    if len(hashtags) > 4:
        logger.error("Voting app accepts only 4 hashtags at the time")
        hashtags = hashtags[:4]

    args.hashtags = hashtags
    return args


def parse_commandline_args():
    argparser = ArgumentParser(
        prog="twittervoting", description="Collect votes using twitter hashtags."
    )

    required = argparser.add_argument_group("require arguments")
    required.add_argument(
        "-ht",
        "--hashtags",
        nargs="+",
        required=True,
        dest="hashtags",
        help=(
            "Space separated list of hashtags that will be used for the voting. \n"
            "Type the hashtags without the hash symbol"
        ),
    )

    args = argparser.parse_args()
    print("AAAAARGS")
    print(args)
    return validated_args(args)
