#!/usr/bin/env python

import requests
from optparse import OptionParser

try:
    from urllib import quote
except ImportError:
    from urllib.parse import quote


GENURL = 'http://memegenerator.co'
INFO = "{0}/PageData/Caption?urlName={{0}}".format(GENURL)
ACTION = "{0}/Xhr/Instance_Caption".format(GENURL)
POPULAR = '{0}/Xhr/Generator_Search?q='.format(GENURL)
SEARCH = '{0}/Xhr/Generator_Search?q={{0}}'.format(GENURL)
IMAGES = 'http://images.memegenerator.co/images/400x/{0}.jpg'
INSTANCE = "http://cdn0.meme.li/instances/300x300/{0}.jpg"


def list_memes(pattern=None):
    memeinfo = []
    if pattern:
        url = SEARCH.format(quote(pattern))
    else:
        url = POPULAR
    result = requests.get(url)
    for m in result.json():
        memeinfo.append({
            'title': m['urlName'],
            'score': str(m['totalVotesScore']),
            'image': m['imageID'],
        })
    memeinfo = sorted(memeinfo, key=lambda k: 0 - int(k['score']))
    return memeinfo


def pp_memes(memelist):
    if len(memelist) > 0:
        keys = [t['title'] for t in memelist]
        keys.sort(key=lambda x: len(x))
        maxlen = len(keys.pop())
        output = ''
        output +=  "{0}  {1}  Template\n".format('Name'.ljust(maxlen),
                                                 'Score'.ljust(6))
        output += "{0}  ------  --------\n".format('-' * maxlen)
        for m in memelist:
            output += "{0}  {1}  {2}\n".format(m['title'].ljust(maxlen),
                                               m['score'].ljust(6),
                                               IMAGES.format(m['image']))
    else:
        output = 'No matches'

    return output


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


def main(options, args):
    output = 'Nothing happened'
    if len(args) == 0:
        if options.memelist or options.search:
            output = pp_memes(list_memes(options.search))
        elif options.version:
            from __init__ import __version__
            output =  __version__
        else:
            parser.error('Requires -s, -l, or args.')
    else:
        title = None  # In case we don't find a title
        if options.search:
            matches = list_memes(options.search)
            if len(matches) > 0:
                title = matches[0]['title']  # default to top scoring match
        else:
            title = args.pop(0)

        if title:
            output = create_meme(title, args)
        else:
            output = "No memes found matching {0}".format(options.search)
    return output


def parse_args(arglist=None):
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
    parser.add_option('-v', '--version', action='store_true',
                      help='show version')
    if arglist:
        return parser.parse_args(arglist)
    else:
        return parser.parse_args()


def cli(arglist=None):
    options, args = parse_args(arglist)
    return main(options, args)


if __name__ == '__main__':
    try:
        print(cli())
    except KeyboardInterrupt:
        pass
