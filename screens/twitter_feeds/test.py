import pycurl
c1 = pycurl.Curl()
c1.setopt(pycurl.URL, 'http://www.twitter.com')
c1.setopt(pycurl.PROXY, '192.168.1.99')
c1.setopt(pycurl.PROXYPORT, 7070)
c1.setopt(pycurl.PROXYTYPE, pycurl.PROXYTYPE_SOCKS5)
c1.perform()

