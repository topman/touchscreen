# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.utils import simplejson

import feedparser

def get_feeds(request):
    FEED_TYPE = {
        "0" : "tweets",
        "1" : "favorate",
    }
    if request.method == "POST":
        data = request.POST
        feeds_type = data.get("type", "")
        feeds_type = FEED_TYPE.get(feeds_type)
        feeds_url = data.get("feeds_url", "")
        num_per_page = data.get("num_per_page", 5)
        page_no = data.get("page_no", 0)

        num_per_page, page_no = int(num_per_page), int(page_no)

        #feeds_url = "http://trac.edgewall.org/timeline?changeset=on&ticket=on&milestone=on&wiki=on&max=50&authors=&daysback=90&format=rss"
        # limit the numbers
        import re
        import urllib2
        import socks
        import socket
        socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "192.168.1.99", 7070)
        socket.socket = socks.socksocket

        return HttpResponse(urllib2.urlopen(feeds_url).read())

        channels = feedparser.parse(feeds_url)
        return HttpResponse(simplejson.dumps(channels), mimetype="application/json")
        total_num = len(channels.entries)
        entries = channels.entries[page_no*num_per_page : (page_no+1)*num_per_page]
        return HttpResponse(simplejson.dumps(entries), mimetype="application/json")

        flag, resp = gen_response(entries, feeds_type)

        if flag:
            response = {
                "status" : "ok",
                "total_num" : total_num,
                "entries" : resp
            }
        else:
            response = {"status" : "error", "reason" : "Rss doesn't have some specific fields"}
    else:
        response = {"status" : "error", "reason" : "Need post request"}
    return HttpResponse(simplejson.dumps(response), mimetype="application/json")

def gen_response(entries, feeds_type):
    mapping = {
        "timeline" : ["title", "author", "link", "updated"],
        "tickets" : ['title', 'link', 'updated'],
        "revision_log" : ["title", "author", "link", "updated"],
    }
    attrs = mapping.get(feeds_type)
    if attrs is None:
        attrs = mapping.get("tickets")
    data = []
    for entry in entries:
        item = {}
        for attr in attrs:
            # rss entry may not have the attr
            try:
                item[attr] = getattr(entry, attr)
            except:
                return False, None
        data.append(item)
    return True, data
        

