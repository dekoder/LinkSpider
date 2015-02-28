from UrlManager import UrlManager
from PathSet import PathSet

pathSet = PathSet()
manager = UrlManager()

def filter(url):

    if not pathSet.dismatch(url):
        return False

    if not manager.addUrl(url):
        return False

    return True

def test():
    urls = [
        'http://a.com/b/c/eee33',
        'http://a.com/b/c/eee34',
        'http://a.com/b/c/eee35',
        'http://a.com/b/c/eee36',
        'http://a.com/b/c33/eee33',
        'http://a.com/b/c34/eee33',
        'http://a.com/b/c35/eee33',
        'http://a.com/b/c37/eee33',
        '/b/c/eee33',
        '/b/c/eee34',
        '/b/c/eee35',
        '/b/c/eee36'
    ]
    for url in urls:
        print filter(url)

test()

