"""
Testing for the get_feeds function for the Trac Feeds plugin
"""

from django.test import TestCase
from django.test.client import Client

from django.core.urlresolvers import reverse

class TracFeedsTest(TestCase):
    def setUp(self):
        self.c = Client()
        self.get_feeds_url = reverse("trac_get_feeds")

    def test_get_feeds(self):
        self.assertNotEqual(self.get_feeds_url, "")
        # testing POST request with correct arguments
        num_per_page = 5
        page_no = 1
        post_data = {
            "rss_type" : "timeline",
            "rss_url" : "http://trac.edgewall.org/timeline?changeset=on&ticket=on&milestone=on&wiki=on&max=50&authors=&daysback=90&format=rss",
            "num_per_page" : num_per_page,
            "page_no" : page_no
        }
        response = self.c.post(self.get_feeds_url, post_data)
        d_res = eval(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(d_res), num_per_page)
        #self.assertEqual(response.content, "")
        # testing GET request which will return []
        response = self.c.get(self.get_feeds_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, "[]")

