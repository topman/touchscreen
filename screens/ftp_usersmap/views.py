# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.utils import simplejson
from datetime import datetime

import feedparser

def get_user_info(request):
    """mock the online ftp users
    """
    import random
    lat = random.randint(50, 70);
    lng = random.randint(-70, -50)
    title = "Mock position"
    ret = """
    <rss version="2.0"><channel>
    <title>%s</title>
    <link>test</link>
    <pubDate>%s</pubDate>
    <item><title>%s</title></item>
    <item><title>%s</title></item>
    <item><title>%s</title></item>
    </channel></rss>
    """%("Test", datetime.now(), title, lat, lng)
    return HttpResponse(ret)

