from bs4 import BeautifulSoup as bs
import hashlib
import sys
import os

def nodeHash(node, level = 0):
    if node.name in [None, "a", "span", "script", "i", "h1", "h2", "h3",
                     "h4", "h5", "noscript", "img", "br", "p", "button",
                     "b", "meta", "li", "link"] \
            or level >= 9:
        return ""
    s = set([node.name])
    for c in node.children:
        s.add(nodeHash(c, level + 1))
    for i in s:
        pass
    h = ""
    #print " " * level, s
    for i in s:
        if i:
            h += i + "#"
    h = hashlib.md5(h).hexdigest()
    #print " " * level, node.name, h
    return h

def hashCount(data):
    return nodeHash(bs(data).html)

if __name__ == "__main__":
    os.system("wget http://tieba.baidu.com/p/" + sys.argv[1] + " -O " + sys.argv[1])
    print hashCount(open(sys.argv[1]).read())
