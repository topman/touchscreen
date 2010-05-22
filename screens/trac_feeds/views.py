# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.utils import simplejson

import feedparser

def get_feeds(request):
    FEED_TYPE = {
        "0" : "timeline",
        "1" : "tickets",
        "2" : "revision_log"
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
        rx_str = "max="
        if feeds_type == "revision_log":
            rx_str = "limit="
        rx = re.compile(r"%s([0-9]+)" % rx_str)
        max_num = rx.findall(feeds_url)
        if max_num == []:
            feeds_url += "%s=50" % rx_str
        elif int(max_num[0]) > 50:
            feeds_url += "%s=50" % rx_str


        channels = feedparser.parse(feeds_url)
        total_num = len(channels.entries)
        entries = channels.entries[page_no*num_per_page : (page_no+1)*num_per_page]

        response = {
            "total_num" : total_num,
            "entries" : gen_response(entries, feeds_type)
        }
    else:
        response = []
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
            item[attr] = getattr(entry, attr)
        data.append(item)
    return data
        

