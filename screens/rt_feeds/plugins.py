from django import forms
from core.models import *
from django.utils.translation import ugettext_lazy as _

class RTFeedsSettings(forms.Form):
    FEEDS_TYPE = (
        ("0", _("timeline")),
        ("1", _("tickets")),
        #("2", _("reports")),
        #("3", _("query")),
        #("4", _("browser")),
        ("3", _("revision_log")),
    )

    feeds_type = forms.ChoiceField(
        label = "RT Feeds type",
        help_text = "Choose one of the rt feeds type",
        initial = "timeline",
        choices = FEEDS_TYPE,
    )

    feeds_url = forms.CharField(
        label = "RT Feeds URL",
        help_text = "URL of the rt feeds to the specified type",
        initial = "http://issues.bestpractical.com/NoAuth/rss/guest/122d2a7aa7b18e1f/?Order=DESC|DESC|ASC|ASC&OrderBy=LastUpdated|Created|Due|Owner&Query=%20Owner%20%3D%20'__CurrentUser__'%20AND%20(%20Status%20%3D%20'new'%20OR%20Status%20%3D%20'open')",
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


class RTFeeds(Screen):
    description = 'RT feeds from a specified rt site'
    template = 'rt_feeds.html'
    config_form = (RTFeedsSettings, ScreenGeneralSettings)
    show='fade'
    hide='fade'
