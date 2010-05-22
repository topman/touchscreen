from django import forms
from core.models import *
from django.utils.translation import ugettext_lazy as _

class TracFeedsSettings(forms.Form):
    FEEDS_TYPE = (
        ("0", _("timeline")),
        ("1", _("tickets")),
        #("2", _("reports")),
        #("3", _("query")),
        #("4", _("browser")),
        ("3", _("revision_log")),
    )

    feeds_type = forms.ChoiceField(
        label = "Trac Feeds type",
        help_text = "Choose one of the trac feeds type",
        initial = "timeline",
        choices = FEEDS_TYPE,
    )

    feeds_url = forms.CharField(
        label = "Trac Feeds URL",
        help_text = "URL of the trac feeds to the specified type",
        initial = "http://trac.edgewall.org/timeline?changeset=on&ticket=on&milestone=on&wiki=on&max=50&authors=&daysback=90&format=rss",
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


class TracFeeds(Screen):
    description = 'Trac feeds from a specified trac site'
    template = 'trac_feeds.html'
    config_form = (TracFeedsSettings, ScreenGeneralSettings)
    show='fade'
    hide='fade'
