from django import forms
from core.models import *
from django.utils.translation import ugettext_lazy as _

class TwitterFeedsSettings(forms.Form):
    FEEDS_TYPE = (
        ("0", _("Tweets")),
        ("1", _("Favorate")),
        #("2", _("reports")),
        #("3", _("query")),
        #("4", _("browser")),
    )

    feeds_type = forms.ChoiceField(
        label = "Twitter Feeds type",
        help_text = "Choose one of the twitter feeds type",
        initial = "timeline",
        choices = FEEDS_TYPE,
    )

    feeds_url = forms.CharField(
        label = "Twitter Feeds URL",
        help_text = "URL of the twitter feeds to the specified type",
        initial = "http://twitter.com/statuses/user_timeline/22250643.rss",
        max_length = 328
    )

    num_per_page = forms.IntegerField(
        label = "feeds number per screen page",
        help_text = "the feeds number shown in one screen page(10 is recommended)",
        initial = 10 
    )
    bypass_cache = forms.ChoiceField(
        label = "whether bypass the cached feeds",
        help_text = "cache will be used to store the requested feeds if set false(false is recommended)",
        initial = "false",
        choices=(("false", 'false'), ("true", 'true'))
        #widget=forms.RadioSelect
    )


class TwitterFeeds(Screen):
    description = 'Twitter feeds from a specified twitter site'
    template = 'twitter_feeds.html'
    config_form = (TwitterFeedsSettings, ScreenGeneralSettings)
    show='fade'
    hide='fade'
