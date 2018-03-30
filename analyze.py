from functools import *
import json
import math

with open("tweets.json", "r") as tweet_db:
    tweets = json.load(tweet_db)


def flatten(xs):
    return reduce(lambda x, y: x + y, xs)


def difference(xs, ys):
    return list(filter(lambda x: x not in ys, xs)) + list(filter(lambda y: y not in xs, ys))


def to_text(tweets):
    return list(map(lambda x: x["content"], tweets))


def to_lowercase(tweets):
    return list(map(lambda x, y: {**x, **{"content": y["content"].lower()}}, tweets, tweets))


def nonempty(tweets):
    return list(filter(lambda x: x["content"] is not "", tweets))


def total_word_count(tweets):
    return reduce(lambda x, y: x + y, list(map(lambda x: len(x["content"].split()), nonempty(tweets))))


def hashtags(tweet):
    return list(filter(lambda x: x[0] == "#", tweet["content"].split()))


def mentions(tweet):
    return list(filter(lambda x: x[0] == "@", tweet["content"].split()))


def all_hashtags(tweets):
    return flatten(list(map(lambda x: hashtags(x), tweets)))


def all_mentions(tweets):
    return flatten(list(map(lambda x: mentions(x), tweets)))


def all_caps_tweets(tweets):
    return list(filter(lambda x: x["content"].isupper(), tweets))


def count_individual_words(tweets):
    return reduce(lambda x, y: dict(x, **y), list(map(lambda x: {x: flatten(list(map(lambda x: x["content"].split(), tweets))).count(x)}, flatten(list(map(lambda x: x["content"].split(), tweets))))))


def count_individual_hashtags(tweets):
    return reduce(lambda x, y: dict(x, **y), list(map(lambda x: {x: all_hashtags(tweets).count(x)}, all_hashtags(tweets))))


def count_individual_mentions(tweets):
    return reduce(lambda x, y: dict(x, **y), list(map(lambda x: {x: all_mentions(tweets).count(x)}, all_mentions(tweets))))


def n_most_common(n, word_count):
    return sorted(word_count.items(), key= lambda x:(-x[1], x))[:n]


def iphone_tweets(tweets):
    return list(filter(lambda x: "iPhone" in x["source"], tweets))


def android_tweets(tweets):
    return list(filter(lambda x: "Android" in x["source"], tweets))


def average_favorites(tweets):
    return int(round(reduce(lambda x, y: x + y, list(map(lambda x: x["favorites"], tweets))) / len(tweets)))


def average_retweets(tweets):
    return int(round(reduce(lambda x, y: x + y, list(map(lambda x: x["retweets"], tweets))) / len(tweets)))


def sort_by_favorites(tweets):
    return sorted(tweets, key=lambda x: x["favorites"])


def sort_by_retweets(tweets):
    return sorted(tweets, key=lambda x: x["retweets"])


def upper_quartile(tweets):
    return tweets[int(math.ceil((3 * (len(tweets) / 4)))) - 1]


def lower_quartile(tweets):
    return tweets[int(math.ceil(len(tweets) / 4)) - 1]


def top_quarter_by(tweets, factor):
    return list(filter(lambda x: x[factor] >= upper_quartile(tweets)[factor], tweets))


def bottom_quarter_by(tweets, factor):
    return list(filter(lambda x: x[factor] <= lower_quartile(tweets)[factor], tweets))
