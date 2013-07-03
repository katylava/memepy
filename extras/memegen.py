import shlex
from util import hook, meme


@hook.command('meme')
@hook.command
def memegen(inp, nick='', chan='', say=None):
    ".meme list <pattern> <n1-12> -- searches memegenerator.net" \
    " | .meme list - <n1-12> -- lists popular meme characters" \
    " | .meme gen|g|-|generate <name> <line1> <line2> -- generates meme" \
    " | .meme fuzzy <pattern> <line1> <line2> -- generate using first match"

    errormsg = "improperly formatted -- do `.help memegen` for help"

    parts = shlex.split(inp.encode('ascii'))
    cmd = parts[0]
    argc = len(parts)

    if cmd == 'list':
        pattern = None
        number = None

        if argc > 1:
            pattern = parts[1]
        if argc > 2:
            number = int(parts[2])

        if pattern and pattern in ['-', 'pop', 'popular', '--']:
            pattern = None

        matches = meme.list_memes(pattern)

        if number and number > len(matches):
            number = None

        if len(matches) == 0:
            result = "no meme characters match search"
        elif not number:
            result = ' '.join(["[%d] %s:%s" % (k+1, v['title'], v['score'])
                              for k, v in enumerate(matches)])
        else:
            match = matches[number-1]
            result = "%s [%s]: %s (%d/%d)" % (
                match['title'],
                match['score'],
                "%s/%s" % (meme.IMAGES, match['image']),
                number,
                len(matches),
            )
    elif cmd in ['gen', 'g', 'generate', '-', 'fuzzy']:
        if argc < 4:
            result = errormsg
        else:
            title = parts[1]
            lines = parts[2:4]
            if cmd == 'fuzzy':
                matches = meme.list_memes(title)
                title = matches[0]['title']
            try:
                result = meme.create_meme(title, lines)
            except Exception, e:
                result = 'error: %s' % e
    else:
        result = errormsg

    return result
