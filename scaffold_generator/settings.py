from django.conf import settings

from .defaults import DEFAULT_FIELDS
from .defaults import DEFAULT_SETTINGS


class ScaffoldGeneratorConfig(dict):
    """dot.notation access to dictionary attributes"""
    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__

    def __init__(self, *args, userkwargs=None, **kwargs):
        super().__init__(*args, **kwargs)
        if not userkwargs:
            userkwargs = {}
        settings_keys = set(DEFAULT_SETTINGS.keys())
        user_settings = {**getattr(settings, 'SCAFFOLD_GENERATOR_SETTINGS', {}), **userkwargs}
        user_settings = {k: v for k, v in user_settings if k in settings_keys}
        config_settings = {
            **DEFAULT_SETTINGS,
            **user_settings,
        }
        for key, value in config_settings.items():
            self[key] = value
        self.post_init()

    def post_init(self):
        self['FIELDS'] = {**DEFAULT_FIELDS, **self['FIELDS']}
