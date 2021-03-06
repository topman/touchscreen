from core.models import Screen, ScreenGeneralSettings
from django import forms

class NetPeopleSettings(forms.Form):
    
    thumbnail_height = forms.IntegerField(
            label='Thumbnail Image Height',
            help_text='The height of the thumbnail images',
            initial=100
    )

    main_height = forms.IntegerField(
            label='Main Image Height',
            help_text='The height of the main image',
            initial=450
    )
    
    scroll_interval = forms.IntegerField(
        label='Scroll Interval',
        help_text='Time between scrolling (in milliseconds). Must be at least 50 more than scroll speed.',
        initial=3000
    )
    
    scroll_speed = forms.IntegerField(
        label='Scroll Speed',
        help_text='Time it takes to scroll a single item (in milliseconds). Must be at least 50 less than scroll interval.',
        initial=1000
    )
    
    auto_rotation_interval = forms.IntegerField(
        label='Auto Rotation Interval',
        help_text='Time between people auto rotations (in milliseconds).',
        initial=10000
    )
    
    rotation_pause_timeout = forms.IntegerField(
        label='Auto Rotation Pause Timeout',
        help_text='Time from when a person is explicitly selected to be shown to when auto rotation starts again (in milliseconds).',
        initial=180000
    )


class screens_net_people(Screen):
    template='net_people.html'
    description="Photos of the employees of Network Services"
    config_form=(NetPeopleSettings, ScreenGeneralSettings)
