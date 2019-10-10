#!/usr/bin/python3

import requests
import argparse
from random import randint


parser = argparse.ArgumentParser(description="Show, random, indiehacker's quotes")
parser.add_argument('-m', '--max_random', metavar='N', type=int,
                    help='max value of random range', default=150)
parser.add_argument('-n', '--number_of_quotes', metavar='N', type=int,
                    help='number of quotes to show', default=1)


BASE_URL = "https://indie-hackers.firebaseio.com/loadingQuotes/{}.json"


def get_random_quote(max_quote):

    data = None

    # while you can't find a valid quote search randomly
    while True :
        # the max value should get from somewhere
        random_quote_index = randint(0, 200)
        url_req = BASE_URL.format( random_quote_index)

        # send request
        r = requests.get(url = url_req)
        data = r.json()

        if data is not None:
            break


    quote = data['quote']
    quote_url = data.get('url', '----')

    byline = data['byline']
    components = byline.split('of')
    author = components[0]

    print("\n%s\n%s" %(author, '='*len(author)))
    print("\tCompany: %s" % (components[1]))
    print("\tQuote: %s" % (quote))
    print("\tURL: %s\n" %(quote_url))



if __name__ == "__main__":

    args = parser.parse_args()
    for i in  range(0, args.number_of_quotes):
        get_random_quote(args.max_random)

