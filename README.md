Indie-Hackers-Quotes
====================


This software retrieve, random or specific, quotes from https://www.indiehackers.com/.

How to
------

*$ python indiequotes.py  ARGS*

arguments:

      -h, --help                  , show this help message and exit
      -m N, --max_random N        , max value of random range (default 150)
      -n N, --number_of_quotes N  , number of quotes to show  (default 1)
      -q N, --quote QUOTE_INDEX   , get quote identified by QUOTE_INDEX


if '--quote' is specified than the sw try to retrieve that specific quote.
If not specified the sw start by default trying to retrieve one random quote.

