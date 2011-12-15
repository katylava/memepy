#!/usr/bin/env python

from pyquery import PyQuery
from urllib import quote

GENURL = 'http://memegenerator.net'
POPULAR = 'memes/popular/alltime'
SEARCH = 'memes/search?q=%s'
IMAGES = 'http://images.memegenerator.net/images/400x'


def list_memes(pattern=None):
    memeinfo = []
    if pattern:
        query = SEARCH % quote(pattern)
        url = '%s/%s' % (GENURL, query)
    else:
        url = '%s/%s' % (GENURL, POPULAR)
    pq = PyQuery(url=url)
    nodes = pq.find('#generatorGallery li div.generator_wide table tr')
    if len(nodes) > 0:
        for n in nodes:
            tq = PyQuery(n)
            memeinfo.append({
                'title': tq.find('.title a')[0].attrib['href'][1:],
                'score': tq.find('.score').text(),
                'image': tq.find('img')[0].attrib['src'].split('/')[-1],
            })
    memeinfo = sorted(memeinfo, key=lambda k: 0 - int(k['score']))
    return memeinfo

def pp_memes(memelist):
    if len(memelist) > 0:
        keys = [t['title'] for t in memelist]
        keys.sort(cmp=lambda x,y: len(x)-len(y))
        maxlen = len(keys.pop())
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
        print "Error: something changed or something weird happened."
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
        print GENURL + postq.find('div.instance_large img')[0].attrib['src']

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
                      help='list meme characters matching search pattern (up to 12)')
    (options, args) = parser.parse_args()

    if len(args) == 0:
        if options.memelist or options.search:
            pp_memes(list_memes(options.search))
    else:
        if options.search:
            matches = list_memes(options.search)
            if len(matches) > 0:
                meme = matches[0]['title'] # default to top scoring match
        else:
            meme = args.pop(0)

        if meme:
            create_meme(meme, args)
        else:
            print "No memes found matching %s" % meme
