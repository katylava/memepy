Installation
============

``pip install meme``

Installs ``meme`` command line tool.

Usage
=====

    Usage: `meme <meme> <line1> <line2>`
    or: `meme -s <pattern> <line1> <line2>`

In the first form you must provide a valid meme name (which can be determined
by running meme.py -l or meme.py -s <pattern> with no arguments).

In the second form the script will use the highest scoring character matching
the search pattern.

Options:
    -h, --help            show this help message and exit
    -l, --list            list popular meme characters (up to 11)
    -s STRING, --search=STRING
                          list meme characters matching search pattern (up to 11)

Examples::

  $ meme Y-U-No "Y U NO" "make command line memes"
  http://cdn0.meme.li/instances/300x300/39417053.jpg

  $ meme.py -s cat "Business Cat" "is most popular cat"
  http://cdn0.meme.li/instances/300x300/39417065.jpg

  $ meme -s cat

      Name                     Score   Template
      -----------------------  ------  --------
      Business-Cat             1400    http://images.memegenerator.co/images/400x/332591.jpg
      Grumpy-Cat-1             1166    http://images.memegenerator.co/images/400x/6541210.jpg
      Chemistry-Cat            975     http://images.memegenerator.co/images/400x/1119726.jpg
      Anxiety-Cat              525     http://images.memegenerator.co/images/400x/1533638.jpg
      Bad-Advice-Cat           119     http://images.memegenerator.co/images/400x/991.jpg
      I-Should-Buy-A-Boat-Cat  50      http://images.memegenerator.co/images/400x/7349397.jpg
      Chronic-Illness-Cat      44      http://images.memegenerator.co/images/400x/1119978.jpg
      Grumpy-Cat-Good          12      http://images.memegenerator.co/images/400x/7366087.jpg
      Sadcat                   7       http://images.memegenerator.co/images/400x/122602.jpg
      Tard-The-Grumpy-Cat      6       http://images.memegenerator.co/images/400x/6636863.jpg
      Diabetic-Cat             -68     http://images.memegenerator.co/images/400x/564471.jpg

  $ meme -l

      Name                                   Score   Template
      -------------------------------------  ------  --------
      Philosoraptor                          9548    http://images.memegenerator.co/images/400x/984.jpg
      Y-U-No                                 9290    http://images.memegenerator.co/images/400x/166088.jpg
      Futurama-Fry                           6388    http://images.memegenerator.co/images/400x/84688.jpg
      Success-Kid                            4559    http://images.memegenerator.co/images/400x/1031.jpg
      The-Most-Interesting-Man-In-The-World  4013    http://images.memegenerator.co/images/400x/2485.jpg
      One-Does-Not-Simply-A                  2594    http://images.memegenerator.co/images/400x/3291562.jpg
      Willywonka                             2172    http://images.memegenerator.co/images/400x/2729805.jpg
      Bad-Luck-Brian-Meme                    1990    http://images.memegenerator.co/images/400x/3459374.jpg
      First-World-Problems-Ii                1691    http://images.memegenerator.co/images/400x/2055789.jpg
      X-All-The-Things                       345     http://images.memegenerator.co/images/400x/1121885.jpg
      Willy-Wonka                            103     http://images.memegenerator.co/images/400x/68999.jpg
