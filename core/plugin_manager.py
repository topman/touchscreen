import urllib2

from django import forms
from muddle.plugins.plugin import Plugin
from muddle.plugins.managers.plugin_manager import PluginManager, PlugableManager

from models import TouchscreenPlugin


class GeneralSettingsForm(forms.Form):
    MAX_OPTIMAL_WIDTH = forms.IntegerField(
        label='Maximum Optimal Width',
        help_text='Maximum width optimal for reading',
        initial=780
    )

    DISPLAY_DURATION = forms.IntegerField(
        label='Default Screen Duration',
        help_text='How long screens will be displayed',
        initial=10000
    )

    TIMEOUT = forms.IntegerField(
        label='Default Screen Timeout',
        help_text='Duration of time without activity before the slide show restarts',
        initial=10000
    )
        
    MSG_SERVER_URL = forms.CharField(
        label='Message Server',
        help_text='The url of the message server',
        initial='http://localhost:9000',
        max_length=128
    )

    MSG_SERVER_QUEUE = forms.CharField(
        label='Message Server Queue',
        help_text='The queue to use on the message server, change if you have multiple displays using the same server', 
        initial='touchscreen',
        max_length=128
    )

class ScreenManager(TouchscreenPlugin, PluginManager):
    """
    Manager that registers screens
    """
    description = 'Manager that registers screens'
    config_form = GeneralSettingsForm
    
    def update_config(self, config):
        """
        Overridden to store copy of config within this class.  By default it
        just unpacks all values to this plugin
        """
        super(TouchscreenPlugin, self).update_config(config)
        self.config = config
    
    def __init__(self, *args, **kwargs):
        TouchscreenPlugin.__init__(self, *args, **kwargs)
        PluginManager.__init__(self)
    
    def get_settings(self):
        """
        Aggregates settings from all the plugins
        """
        touchscreen_settings = {'general':self.config.config}
        return touchscreen_settings

    def register(self, screen):
        super(ScreenManager, self).register(screen)
        try:
            urllib2.urlopen('%s&m=slideshow,enable,%s' % (self.MSG_SEND_URL,screen.name()))
        except:
            pass

    def deregister(self, screen):
        super(ScreenManager, self).deregister(screen)
        try:
            urllib2.urlopen('%s&m=slideshow,disable,%s' % (self.MSG_SEND_URL,screen.name()))
        except:
            pass


class ScreenAnimationManager(PlugableManager):
    """
    Manager that registers screens
    """
    description = 'Manager that registers screen animations'