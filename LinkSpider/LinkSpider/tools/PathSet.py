from urlparse import urlparse

class PathSet:
    """
    filter same type of urls.
    /x1 /x2 are same in type.
    """
    def __init__(self):
        self.numStyleSet = set()

    def __getNumStyle(self, url):
        rs = urlparse(url)
        site = rs.scheme + '://' + rs.netloc
        pieces = filter(lambda x:x, rs.path.split('/'))
        matchs = []
        for piece in pieces:
            match = ''
            for i in range(len(piece)):
                if 47 < ord(piece[i]) < 58: # piece[i] is a number
                    match += '?'
                else:
                    match += piece[i]
            matchs.append(match)
        return site + '#' + '#'.join(matchs)

    def dismatch(self, url):
        newMatch = self.__getNumStyle(url)
        if newMatch not in self.numStyleSet:
            self.numStyleSet.add(newMatch)
            return True
        else:
            return False

def testMatch():
    ps = PathSet()
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
        print ps.dismatch(url)

if __name__ == "__main__":
    testMatch()

