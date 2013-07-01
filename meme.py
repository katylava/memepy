#!/usr/bin/env python

from pyquery import PyQuery
from urllib import quote

GENURL = 'http://memegenerator.co'
POPULAR = 'memes/top/alltime'
SEARCH = 'memes/search?q=%s'
IMAGES = 'http://images.memegenerator.co/images/400x'


def list_memes(pattern=None):
    memeinfo = []
    if pattern:
        query = SEARCH % quote(pattern)
        url = '%s/%s' % (GENURL, query)
    else:
        url = '%s/%s' % (GENURL, POPULAR)
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
        print "%s  %s  Template" % ('Name'.ljust(maxlen), 'Score'.ljust(6))
        print "%s  ------  --------" % ('-' * maxlen)
        for m in memelist:
            print '%s  %s  %s' % (m['title'].ljust(maxlen),
                                  m['score'].ljust(6),
                                  "%s/%s" % (IMAGES, m['image']))
    else:
        print 'No matches'


def create_meme(title, args):
    url = "%s/%s" % (GENURL, title)
    pq = PyQuery(url=url)
    form = pq.find('div.instance_form_create_small form')
    if len(form) == 0:
        return "Error: something changed or something weird happened."
    else:
        url = "%s%s" % (GENURL, form[0].attrib['action'])
        data = {
            'languageCode': 'en',
            'generatorID': form.find('#generatorID').val(),
            'imageID': form.find('#imageID').val(),
            'text0': args[0],
            'text1': len(args) > 1 and args[1] or '',
        }
        postq = PyQuery(url=url, data=data, method='post')
        return postq.find('div.instance_large img')[0].attrib['src']

if __name__ == '__main__':
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

    try:

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
                print "No memes found matching %s" % meme

    except KeyboardInterrupt:
        pass
