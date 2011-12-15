Installation
============

Place meme.py somewhere on your PATH. Requires PyQuery.

Usage
=====

    Usage: `meme.py <meme> <line1> <line2>`
    or: `meme.py -s <pattern> <line1> <line2>`

In the first form you must provide a valid meme name (which can be determined
by running meme.py -l or meme.py -s <pattern> with no arguments).

In the second form the script will use the highest scoring character matching
the search pattern.

Options:
    -h, --help            show this help message and exit
    -l, --list            list popular meme characters (up to 12)
    -s STRING, --search=STRING
                          list meme characters matching search pattern (up to 12)

Examples::

  $ meme.py Y-U-No "Y U NO" "make command line memes"
  http://memegenerator.net/cache/instances/400x/11/12003/12291442.jpg

  $ meme.py -s cat "Business Cat" "is most popular cat"
  http://memegenerator.net/cache/instances/400x/11/12003/12291472.jpg

  $ meme.py -s cat

      Business-Cat         521     http://images.memegenerator.net/images/400x/332591.jpg
      Chemistry-Cat        316     http://images.memegenerator.net/images/400x/1119726.jpg
      Bad-Advice-Cat       46      http://images.memegenerator.net/images/400x/991.jpg
      Chronic-Illness-Cat  11      http://images.memegenerator.net/images/400x/1119978.jpg
      Science-Cat          10      http://images.memegenerator.net/images/400x/1121079.jpg
      Serious-Cat          6       http://images.memegenerator.net/images/400x/10362.jpg
      Winnipeg-Cat         3       http://images.memegenerator.net/images/400x/1396.jpg
      Wisdom-Cat           3       http://images.memegenerator.net/images/400x/970.jpg
      Sadcat               2       http://images.memegenerator.net/images/400x/122602.jpg
      Advice-Cat           1       http://images.memegenerator.net/images/400x/20096.jpg
      Poker-Cat            -1      http://images.memegenerator.net/images/400x/1122133.jpg
      A-Cat                -3      http://images.memegenerator.net/images/400x/1102702.jpg

  $ meme.py -l

      Philosoraptor                          3022    http://images.memegenerator.net/images/400x/984.jpg
      Y-U-No                                 2476    http://images.memegenerator.net/images/400x/166088.jpg
      Socially-Awkward-Penguin               1524    http://images.memegenerator.net/images/400x/983.jpg
      Forever-Alone                          1415    http://images.memegenerator.net/images/400x/142442.jpg
      Insanity-Wolf                          1343    http://images.memegenerator.net/images/400x/20.jpg
      Futurama-Fry                           1292    http://images.memegenerator.net/images/400x/84688.jpg
      Trollface                              1270    http://images.memegenerator.net/images/400x/269.jpg
      Foul-Bachelor-Frog                     1269    http://images.memegenerator.net/images/400x/203.jpg
      Success-Kid                            1130    http://images.memegenerator.net/images/400x/1031.jpg
      Joseph-Ducreux                         1104    http://images.memegenerator.net/images/400x/42.jpg
      Courage-Wolf                           881     http://images.memegenerator.net/images/400x/24.jpg
      The-Most-Interesting-Man-In-The-World  808     http://images.memegenerator.net/images/400x/2485.jpg


Future
======

* provide option to use the API instead if a username and password are specified
* Package this "properly".
* Allow user config in ~/.memepy
* Automatically copy url to clipboard
* Option to send to imgur.com and get that url instead
