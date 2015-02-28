#/usr/bin/env python

import os, sys
from urlparse import urlparse

def usage():
    print ''
    print 'Usage: %s --l=<start link> [--d=<dmoains>] [--s=<file name>]'
    print ''
    print ' ' * 5, 'l: link, Start Link for crawl. like http://a.com/b/c.php'
    print ' ' * 5, 'd: domains, Allowed domains, seperate by , like --domains=a.com,b.com'
    print ' ' * 5, "s: store, Store File's Name"
    print ''
    print 'Warnig: LINK MUST INCLUDE SCHEME, i.e. http://a.com, not a.com'
    print ''


if __name__ == '__main__':
    os.chdir('./LinkSpider/')

    link = ''
    domains = []
    store = 'store'

    argc = len(sys.argv)
    cur = 1
    while cur < argc:
        s = sys.argv[cur]
        if len(s) > 3 and s[0:2] == '--':
            if s[2:4] == 'l=':
                link = s[4:]
            if s[2:4] == 'd=':
                domains = s[4:].split(',')
            if s[2:4] == 's=':
                if s[4:]:
                    store = s[4:]
        cur += 1

    if link == '' or link.find("://") == -1:
        usage()
        exit()

    parse = urlparse(link)
    if not domains:
        domains = [parse.netloc]
    domains = map(lambda x : "'" + x + "'", domains)
    store = '#'.join([parse.netloc, parse.path, store])

    fd = open('./LinkSpider/config.py', 'w')
    fd.writelines("start_link = '%s'\n" % link)
    fd.writelines("store_path = '%s'\n" % store)
    fd.writelines("domains = [%s]\n" % ','.join(domains))
    fd.close()

    os.system('scrapy crawl urls')

