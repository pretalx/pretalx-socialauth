from django.apps import AppConfig
from django.utils.translation import gettext_lazy


class PluginApp(AppConfig):
    name = 'pretalx_socialauth'
    verbose_name = 'OAuth2 for pretalx'

    class PretalxPluginMeta:
        name = gettext_lazy('OAuth2 for pretalx')
        author = 'Tobias Kunze'
        description = gettext_lazy(
            "Use other websites, like GitHub or Twitter, to allow users to log in to pretalx."
        )
        visible = True
        version = '0.0.0'

    def ready(self):
        from . import signals  # NOQA


default_app_config = 'pretalx_socialauth.PluginApp'
