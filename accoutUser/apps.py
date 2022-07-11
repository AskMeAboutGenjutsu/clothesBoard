from django.apps import AppConfig


class AccoutuserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accoutUser'

    def ready(self):
        from . import signals
