from django.apps import AppConfig


class CbsappConfig(AppConfig):
    name = 'cbsapp'

    def ready(self):
        import users.signals
