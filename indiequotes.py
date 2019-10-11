#!/usr/bin/python3

import requests
import argparse
from random import randint


parser = argparse.ArgumentParser(description="Show, random, indiehacker's quotes")
parser.add_argument('-m', '--max_random', metavar='N', type=int,
                    help='max value of random range', default=150)
parser.add_argument('-n', '--number_of_quotes', metavar='N', type=int,
                    help='number of quotes to show', default=1)


BASE_URL = 'https://indie-hackers.firebaseio.com/loadingQuotes/{}.json'



def render_quote(quote):
    header_str = 'Quote: #%s' % quote['quote_index']
    print("\n%s\n%s" % (header_str, '='*len(header_str)))
    print("\"%s\"" % quote['quote'])
    print("\n%s, %s - %s" %(quote['author'], quote['company'], quote['mrr']))
    print("%s\n" %(quote['url']))

def get_random_quote(max_quote):

    data = None
    random_quote_index = None
    res = dict()

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
    author = components[0].rstrip()
    round_bracket_index = components[1].find('(')
    company = components[1][0: round_bracket_index - 1]
    mrr = components[1][round_bracket_index +1 : -1]

    res['quote'] = quote
    res['author'] = author
    res['company'] = company
    res['mrr'] = mrr
    res['quote_index'] = random_quote_index
    res['url'] = quote_url

    return res


if __name__ == "__main__":

    args = parser.parse_args()
    for i in  range(0, args.number_of_quotes):
        quote = get_random_quote(args.max_random)
        render_quote(quote)

