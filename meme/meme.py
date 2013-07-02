#!/usr/bin/env python

import requests
from pyquery import PyQuery
from urllib import quote

GENURL = 'http://memegenerator.co'
INFO = "{0}/PageData/Caption?urlName={{0}}".format(GENURL)
ACTION = "{0}/Xhr/Instance_Caption".format(GENURL)
POPULAR = '{0}/memes/top/alltime'.format(GENURL)
SEARCH = '{0}/memes/search?q={{0}}'.format(GENURL)
IMAGES = 'http://images.memegenerator.co/images/400x/{0}'
INSTANCE = "http://cdn0.meme.li/instances/300x300/{0}.jpg"


def list_memes(pattern=None):
    memeinfo = []
    if pattern:
        query = SEARCH.format(quote(pattern))
        url = SEARCH.format(query)
    else:
        url = POPULAR
    pq = PyQuery(url=url)
    nodes = pq.find('ul.gallery li div.generator')
    if len(nodes) > 0:
        for n in nodes:
            tq = PyQuery(n)
            memeinfo.append({
                'title': tq.find('a')[0].attrib['href'][1:],
                'score': tq.find('div.info div.score').text(),
                'image': tq.find('a img')[0].attrib['src'].split('/')[-1],
            })
    memeinfo = sorted(memeinfo, key=lambda k: 0 - int(k['score']))
    return memeinfo


def pp_memes(memelist):
    if len(memelist) > 0:
        keys = [t['title'] for t in memelist]
        keys.sort(cmp=lambda x, y: len(x) - len(y))
        maxlen = len(keys.pop())
        print "{0}  {1}  Template".format('Name'.ljust(maxlen),
                                          'Score'.ljust(6))
        print "{0}  ------  --------".format('-' * maxlen)
        for m in memelist:
            print '{0}  {1}  {2}'.format(m['title'].ljust(maxlen),
                                         m['score'].ljust(6),
                                         IMAGES.format(m['image']))
    else:
        print 'No matches'


def create_meme(title, args):
    memeinfo = requests.get(INFO.format(title))
    data = {
        'languageCode': 'en',
        'urlName': title,
        'imageID': memeinfo.json()['Item']['imageID'],
        'text0': args[0],
        'text1': len(args) > 1 and args[1] or '',
    }
    result = requests.post(ACTION, data=data)
    instance_id = result.json()['instanceID']
    return INSTANCE.format(instance_id)


def cli():
    from optparse import OptionParser
    usage = ("usage: %prog <meme> <line1> <line2>\n"
             "or: %prog -s <pattern> <line1> <line2>\n"
             "In the first form you must provide a valid meme name (which"
             " can be determined by running %prog -l or %prog -s <pattern>"
             " with no arguments).\n"
             "In the second form the script will use the highest scoring"
             " character matching the search pattern.")
    parser = OptionParser(usage=usage)
    parser.add_option('-l', '--list', action='store_true',
                      dest='memelist', default=False,
                      help='list popular meme characters (up to 12)')
    parser.add_option('-s', '--search', metavar='STRING',
                      help='list meme characters matching search pattern'
                           '(up to 12)')
    (options, args) = parser.parse_args()

    if len(args) == 0:
        if options.memelist or options.search:
            pp_memes(list_memes(options.search))
        else:
            parser.error('Requires -s, -l, or args.')
    else:
        if options.search:
            matches = list_memes(options.search)
            if len(matches) > 0:
                meme = matches[0]['title']  # default to top scoring match
        else:
            meme = args.pop(0)

        if meme:
            print create_meme(meme, args)
        else:
            print "No memes found matching {0}".format(meme)


if __name__ == '__main__':
    try:
        cli()
    except KeyboardInterrupt:
        pass
