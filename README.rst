Installation
============

``pip install meme``

Installs ``meme`` command line tool.

**To create memes, you need to have an account with http://memegenerator.co.**

Usage
=====

Usage:
    meme -u <username> -p <password> <meme> <line1> <line2>
or:
    meme -u <username> -p <password> -s <pattern> <line1> <line2>

In the first form you must provide a valid meme name (which can be determined
by running `meme -l` or `meme -s <pattern>` with no arguments).

In the second form the script will use the highest scoring character matching
the search pattern. Since the search API does not return these pre-sorted, the
actual most popular matching meme may not show up in the results -- so be
specific.

NOTE: You must have a memegenerator.co user account to **create** a meme!
(To list popular or search memes you do not need a username and password.)


Options:
  -h, --help            show this help message and exit
  -l, --list            list popular meme characters (up to 24)
  -s PATTERN, --search=PATTERN
                        list meme characters matching search pattern (up to
                        24)
  -u USERNAME, --username=USERNAME
                        Your memegenerator username
  -p PASSWORD, --password=PASSWORD
                        Your memegenerator password
  -v, --version         show version

Examples::

  $ meme -u <username> -p <password> Y-U-No "memegenerator" "y u no stay the same"
  http://cdn.memegenerator.net/instances/400x/39653192.jpg

  $ meme -u <username> -s cat "i'm grumpy" "because i miss business cat"
  http://cdn.memegenerator.net/instances/400x/39653303.jpg

  $ meme -s cat

      Name                       Score   Template
      -------------------------  ------  --------
      Grumpy-Cat-1               1166    http://cdn.memegenerator.net/images/400x/6541210.jpg
      I-Should-Buy-A-Boat-Cat    50      http://cdn.memegenerator.net/images/400x/7349397.jpg
      Grumpy-Cat-Santa-Hat       39      http://cdn.memegenerator.net/images/400x/7403729.jpg
      Newspaper-Cat-Realization  32      http://cdn.memegenerator.net/images/400x/7605130.jpg
      Rich-Cat                   16      http://cdn.memegenerator.net/images/400x/7442025.jpg
      Sophisticated-Cat          14      http://cdn.memegenerator.net/images/400x/7342111.jpg
      Grumpy-Cat-Good            12      http://cdn.memegenerator.net/images/400x/7366087.jpg
      Grumpy-Cat-On-Christmas    8       http://cdn.memegenerator.net/images/400x/7253273.jpg
      Angry-Cat-Meme             7       http://cdn.memegenerator.net/images/400x/7974429.jpg
      Tard-The-Grumpy-Cat        6       http://cdn.memegenerator.net/images/400x/6636863.jpg
      Bane-Cat                   5       http://cdn.memegenerator.net/images/400x/5780845.jpg
      No-Cat                     4       http://cdn.memegenerator.net/images/400x/7374750.jpg
      Grumpy-Cat-Happy-Version   3       http://cdn.memegenerator.net/images/400x/7569582.jpg
      Happy-Grumpy-Cat-2         3       http://cdn.memegenerator.net/images/400x/7531915.jpg
      Grumpy-Cat-Face            3       http://cdn.memegenerator.net/images/400x/6562520.jpg
      Grumpy-Face-Cat            3       http://cdn.memegenerator.net/images/400x/6541691.jpg
      Two-Talking-Cats           2       http://cdn.memegenerator.net/images/400x/4668498.jpg
      Thinking-Cat               1       http://cdn.memegenerator.net/images/400x/7698560.jpg
      Good-Grumpy-Cat-2          1       http://cdn.memegenerator.net/images/400x/7486197.jpg
      Grumpy-Cat-                1       http://cdn.memegenerator.net/images/400x/7390698.jpg
      Mr-Angry-Cat               1       http://cdn.memegenerator.net/images/400x/6717793.jpg
      Frowning-Cat               1       http://cdn.memegenerator.net/images/400x/6628499.jpg
      Starcon-2-Vindicator       1       http://cdn.memegenerator.net/images/400x/5772578.jpg
      Conspiracy-Cat             1       http://cdn.memegenerator.net/images/400x/5189714.jpg

  $ meme -l

      Name                                   Score   Template
      -------------------------------------  ------  --------
      Philosoraptor                          9548    http://cdn.memegenerator.net/images/400x/984.jpg
      Y-U-No                                 9290    http://cdn.memegenerator.net/images/400x/166088.jpg
      Futurama-Fry                           6388    http://cdn.memegenerator.net/images/400x/84688.jpg
      Good-Guy-Greg                          5607    http://cdn.memegenerator.net/images/400x/699717.jpg
      Success-Kid                            4559    http://cdn.memegenerator.net/images/400x/1031.jpg
      The-Most-Interesting-Man-In-The-World  4013    http://cdn.memegenerator.net/images/400x/2485.jpg
      Forever-Alone                          3436    http://cdn.memegenerator.net/images/400x/142442.jpg
      Trollface                              3275    http://cdn.memegenerator.net/images/400x/269.jpg
      Socially-Awkward-Penguin               3226    http://cdn.memegenerator.net/images/400x/983.jpg
      Insanity-Wolf                          3181    http://cdn.memegenerator.net/images/400x/20.jpg
      Joseph-Ducreux                         2661    http://cdn.memegenerator.net/images/400x/42.jpg
      One-Does-Not-Simply-A                  2594    http://cdn.memegenerator.net/images/400x/3291562.jpg
      Conspiracy-Keanu                       2320    http://cdn.memegenerator.net/images/400x/1986282.jpg
      Foul-Bachelor-Frog                     2241    http://cdn.memegenerator.net/images/400x/203.jpg
      Willywonka                             2172    http://cdn.memegenerator.net/images/400x/2729805.jpg
      Scumbag-Steve                          2088    http://cdn.memegenerator.net/images/400x/366130.jpg
      Bad-Luck-Brian-Meme                    1990    http://cdn.memegenerator.net/images/400x/3459374.jpg
      Yo-Dawg                                1926    http://cdn.memegenerator.net/images/400x/108785.jpg
      Annoying-Facebook-Girl                 1770    http://cdn.memegenerator.net/images/400x/876097.jpg
      First-World-Problems-Ii                1691    http://cdn.memegenerator.net/images/400x/2055789.jpg
      All-The-Things                         1513    http://cdn.memegenerator.net/images/400x/1985197.jpg
      Grumpy-Cat-1                           1166    http://cdn.memegenerator.net/images/400x/6541210.jpg
      I-Dont-Always                          1086    http://cdn.memegenerator.net/images/400x/2485.jpg
      Sunny-Student                          -1520   http://cdn.memegenerator.net/images/400x/1702950.jpg
