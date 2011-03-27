#!/usr/bin/env python

from pyquery import PyQuery

GENURL = 'http://memegenerator.net/Instance/CreateOrEdit'
GENERATORS = {
  'ANTEATER'          : ('AdviceDogSpinoff' , 41191   , 'anteater'                              ,              ) ,
  'A_DODSON'          : ('AdviceDogSpinoff' , 106375  , 'Antoine-Dodson'                        ,              ) ,
  'A_DOG'             : ('AdviceDogSpinoff' , 940     , 'Advice-Dog'                            ,              ) ,
  'A_FATHER'          : ('AdviceDogSpinoff' , 1436    , 'High-Expectations-Asian-Father'        ,              ) ,
  'BEAR-GRYLLS'       : ('AdviceDogSpinoff' , 89714   , 'Bear-Grylls'                           ,              ) ,
  'BUTTHURT_DWELLER'  : ('AdviceDogSpinoff' , 1438    , 'Butthurt-Dweller'                      ,              ) ,
  'B_FROG'            : ('AdviceDogSpinoff' , 1211    , 'Foul-Bachelorette-Frog'                ,              ) ,
  'B_FROG2'           : ('AdviceDogSpinoff' , 1045    , 'Foul-Bachelor-Frog'                    ,              ) ,
  'COOL_STORY_HOUSE'  : ('AdviceDogSpinoff' , 16948   , 'cool-story-bro-house'                  ,              ) ,
  'CREEPER'           : ('AdviceDogSpinoff' , 173501  , 'Minecraft-Creeper'                     ,              ) ,
  'C_WOLF'            : ('AdviceDogSpinoff' , 931     , 'Courage-Wolf'                          ,              ) ,
  'F_FRY'             : ('AdviceDogSpinoff' , 84688   , 'Futurama-Fry'                          ,              ) ,
  'G_GRANDPA'         : ('AdviceDogSpinoff' , 185650  , 'Grumpy-Grandpa'                        ,              ) ,
  'H_MERMAID'         : ('AdviceDogSpinoff' , 405224  , 'Hipster-Mermaid'                       ,              ) ,
  'I_DONT_ALWAYS'     : ('AdviceDogSpinoff' , 38926   , 'The-Most-Interesting-Man-in-the-World' ,              ) ,
  'I_WOLF'            : ('AdviceDogSpinoff' , 926     , 'Insanity-Wolf'                         ,              ) ,
  'J_DUCREUX'         : ('AdviceDogSpinoff' , 1356    , 'Joseph-Ducreux'                        ,              ) ,
  'KEANU'             : ('AdviceDogSpinoff' , 47718   , 'Keanu-reeves'                          ,              ) ,
  'MINECRAFT'         : ('AdviceDogSpinoff' , 122309  , 'Minecraft'                             ,              ) ,
  'O-RLY-OWL'         : ('AdviceDogSpinoff' , 117041  , 'O-RLY-OWL'                             , 'ORLY???'    ) ,
  'OBAMA'             : ('AdviceDogSpinoff' , 1332    , 'Obama-'                                ,              ) ,
  'PATRICK'           : ('AdviceDogSpinoff' , 62223   , 'Push-it-somewhere-else-Patrick'        ,              ) ,
  'PHILOSORAPTOR'     : ('AdviceDogSpinoff' , 984     , 'Philosoraptor'                         ,              ) ,
  'P_OAK'             : ('AdviceDogSpinoff' , 24321   , 'Professor-Oak'                         ,              ) ,
  'SCUMBAG'           : ('AdviceDogSpinoff' , 364688  , 'Scumbag-Steve'                         ,              ) ,
  'SERIOUS_FISH'      : ('AdviceDogSpinoff' , 6374627 , 'Spongebob-Serious-Fish'                ,              ) ,
  'SNOB'              : ('AdviceDogSpinoff' , 2994    , 'Snob'                                  ,              ) ,
  'SPARTA'            : ('AdviceDogSpinoff' , 1013    , 'sparta'                                ,              ) ,
  'SPIDERMAN'         : ('AdviceDogSpinoff' , 1037    , 'Question-Spiderman'                    ,              ) ,
  'SWEDISH_CHEF'      : ('AdviceDogSpinoff' , 186651  , 'Swedish-Chef'                          ,              ) ,
  'S_AWKWARD_PENGUIN' : ('AdviceDogSpinoff' , 983     , 'Socially-Awkward-Penguin'              ,              ) ,
  'TOWNCRIER'         : ('AdviceDogSpinoff' , 434537  , 'Towncrier'                             ,              ) ,
  'TROLLFACE'         : ('AdviceDogSpinoff' , 1030    , 'Troll-Face'                            ,              ) ,
  'UNICORN_BOY'       : ('AdviceDogSpinoff' , 57022   , 'unicorn-boy'                           ,              ) ,
  'US_POINT'          : ('AdviceDogSpinoff' , 131083  , 'Uncle-Sam-Point'                       , 'I WANT YOU' ) ,
  'V_BABY'            : ('AdviceDogSpinoff' , 11140   , 'Victory-Baby'                          ,              ) ,
  'XZIBIT'            : ('AdviceDogSpinoff' , 3114    , 'XZIBIT'                                ,              ) ,
  'Y_U_NO'            : ('AdviceDogSpinoff' , 165241  , 'Y-U-NO'                                , 'Y U NO'     ) ,
  'BATMAN'            : ('Vertical'         , 148359  , 'batman-panal-ryan'                     ,              ) ,
  'INCEPTION'         : ('Vertical'         , 107949  , 'Inception'                             ,              ) ,
  'NEO'               : ('Vertical'         , 173419  , 'Neo'                                   ,              ) ,
  'THE_ROCK'          : ('Vertical'         , 417195  , 'The-Rock-driving'                      ,              ) ,
}


def create_meme(data):
    pq = PyQuery(url=GENURL, data=data, method='post')
    return pq.find('a img.large').attr('src')

def get_meme_url(meme):
    gen = GENERATORS.get(meme)
    if gen:
        return 'http://images.memegenerator.net/%s/File/%d/%s.jpg' % (gen[2], gen[1], gen[2])
    else:
        return None

def list_memes(pattern=None):
    memeinfo = []
    pattern = pattern and pattern.lower()
    for optname, specs in GENERATORS.items():
        if not pattern or (pattern in optname.lower() or pattern in specs[2].lower()):
            memeinfo.append((optname, specs[2]))
    memeinfo.sort()
    return memeinfo

def pp_memes(memelist):
    if len(memelist) > 0:
        keys = [t[0] for t in memelist]
        keys.sort(cmp=lambda x,y: len(x)-len(y))
        maxlen = len(keys.pop())
        for k,m in memelist:
            print '%s  %s' % (k.ljust(maxlen), m)
    else:
        print 'No matches'


if __name__ == '__main__':
    from optparse import OptionParser
    parser = OptionParser(usage="usage: %prog <meme> <line1> [additional lines...]")
    parser.add_option('-l', '--list', action='store_true', dest='memelist', default=False, help='list all available memes')
    parser.add_option('-s', '--search', help='list memes with name or option containing string')
    parser.add_option('-p', '--preview_url', default=False, help="Prints the URL for the meme's base image. Does not generate.")
    (options, args) = parser.parse_args()

    if len(args) == 0:
        if options.memelist or options.search:
            pp_memes(list_memes(options.search))
        if options.preview_url:
            print get_meme_url(options.preview_url)
    else:
        meme = GENERATORS.get(args.pop(0))
        if meme:
            data = {
                'templateType': meme[0],
                'templateID': meme[1],
                'generatorName': meme[2],
            }
            idx = 0
            if len(meme) == 4:
                data.update({'text0': meme[3]})
                idx = 1
            for line in args:
                data.update({'text%d' % idx: line})
                idx += 1
            print create_meme(data)
        else:
            print 'No meme specified for "%s"' % meme
