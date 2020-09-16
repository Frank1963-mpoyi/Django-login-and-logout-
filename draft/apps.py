from django.apps import AppConfig


class DraftConfig(AppConfig):
    name = 'draft'
    
    def ready(self):
        import draft.signals


 #from signals.py
    