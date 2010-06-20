import urllib
import urllib2

SERVER = "http://localhost:9000/"

mapping = {
    "0" : """c=1&q=touchscreen&u=touchscreen&m=["slideshow","show","screens_osl_people"]""",
    "1" : """c=1&q=touchscreen&u=touchscreen&m=["slideshow","show","screens_osl_about"]""",
    "2" : """c=1&q=touchscreen&u=touchscreen&m=["slideshow","show","TracFeeds"]""",
}

while True:
    data = raw_input("Enter the command: 0-screens_osl_people, 1-screens_osl_about, 2-screens_trac_feeds, q:quit\n")
    if data == "q":
        break
    command = mapping.get(data, None)
    if data is not None:
        urllib2.urlopen(SERVER + "?" + command)

