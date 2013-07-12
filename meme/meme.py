#!/usr/bin/env python
"""
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
"""

import os
import requests
from optparse import OptionParser

# try:
#     import ConfigParser as configparser
# except ImportError:
#     import configparser

try:
    from urllib import quote
except ImportError:
    from urllib.parse import quote


# TODO: store u/p in config file
# CONFIG_PATH = os.path.expanduser(os.path.join('~', '.meme'))

FIX_MEME = "Time to fix meme again. Check https://pypi.python.org/pypi/meme" \
           " for notice that it's being fixed. If no notice, then ping" \
           " me @katylava."

GENURL = 'http://version1.api.memegenerator.co'

POPULAR_URL = '{0}/Generators_Select_ByPopular'.format(GENURL)
POPULAR_DAT = {
    'pageIndex': '0',
    'pageSize': '24',
    'days': '',
}

SEARCH_URL = '{0}/Generators_Search'.format(GENURL)
SEARCH_DAT = {
    'q': None,
    'pageIndex': '0',
    'pageSize': '24',
}

INFO_URL = "{0}/Generator_Select_ByUrlNameOrGeneratorID".format(GENURL)
INFO_DAT = {'urlName': None}

ACTION_URL = "{0}/Instance_Create".format(GENURL)
ACTION_DAT = {
    'username': None,
    'password': None,
    'languageCode': 'en',
    'generatorID': None,
    'imageID': None,
    'text0': None,
    'text1': None,
}


def get_image_id_from_url(url):
    return os.path.splitext(os.path.basename(url))[0]


def list_memes(pattern=None):
    memeinfo = []
    if pattern:
        url = SEARCH_URL
        SEARCH_DAT.update({'q': pattern})
        params = SEARCH_DAT
    else:
        url = POPULAR_URL
        params = POPULAR_DAT

    result = requests.get(url, params=params).json()
    if not result.get('success', False):
        if result.get('errorMessage', None):
            return result['errorMessage']
        else:
            return FIX_MEME

    for m in result['result']:
        memeinfo.append({
            'title': m['urlName'],
            'score': str(m['totalVotesScore']),
            'generator': str(m['generatorID']),
            'image': m['imageUrl'],
            'rank': m['ranking'],
        })
    memeinfo.sort(key=lambda x: 0 - int(x['score']))
    return memeinfo


def pp_memes(memelist):
    if not isinstance(memelist, list):
        output = memelist
    elif len(memelist) > 0:
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
                                               m['image'])
    else:
        output = 'No matches'

    return output


def create_meme(title, args, options):
    INFO_DAT.update({'urlName': title})
    result, message = get_api_result(INFO_URL, params=INFO_DAT)
    if result:
        ACTION_DAT.update({
            'username': options.username,
            'password': options.password,
            'generatorID': result['generatorID'],
            'imageID': get_image_id_from_url(result['imageUrl']),
            'text0': args[0],
            'text1': len(args) > 1 and args[1] or '',
        })
    else:
        return message

    result, message = get_api_result(ACTION_URL, params=ACTION_DAT)
    if result:
        return result['instanceImageUrl']
    else:
        return message


def get_api_result(*args, **kwargs):
    response = requests.get(*args, **kwargs)
    result = None
    message = FIX_MEME
    try:
        jsondata = response.json()
    except ValueError:
        pass # out is already set for this state
    else:
        if jsondata.get('success', False):
            result = jsondata['result']
            message = None
        elif jsondata.get('errorMessage', False):
            message = jsondata['errorMessage']
    return result, message


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
            output = create_meme(title, args, options)
        else:
            output = "No memes found matching {0}".format(options.search)
    return output


def parse_args(arglist=None):
    usage = globals()['__doc__']
    parser = OptionParser(usage=usage)
    parser.add_option('-l', '--list', action='store_true',
                      dest='memelist', default=False,
                      help='list popular meme characters (up to 24)')
    parser.add_option('-s', '--search', metavar='PATTERN',
                      help='list meme characters matching search pattern'
                           ' (up to 24)')
    parser.add_option('-u', '--username', help="Your memegenerator username")
    parser.add_option('-p', '--password', help="Your memegenerator password")
    parser.add_option('-v', '--version', action='store_true',
                      help='show version')
    # TODO: add language code option
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
