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

As an example:
Enter the following command:

      `$ python indiequotes.py`

Running this command will give an output similar to this:

      Quote: #66
      ==========
      "Ideas are worth nothing unless you make it. Test your ideas quickly and keep improving."

      Harry Chen,  Altcademy - $7K/mo
      https://www.indiehackers.com/interview/keeping-things-lean-and-growing-my-online-course-business-583b7d1f8b

Another option is to specify the quote index:

      python indiequotes.py --q 12
      
This would give the following result:

      Quote: #12
      ==========
      "Don’t look to your competitors for inspiration. Get a sense of your market, but then push past it."

      Diony McPherson,  Paperform - $26K/mo
      https://www.indiehackers.com/interview/how-i-risked-it-all-by-building-a-24k-mo-business-with-my-spouse-69c977f314
      
      
