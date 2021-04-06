from django.apps import AppConfig


class MainConfig(AppConfig):
    name = 'main'
    verbose_name = 'برنامه‌ی اصلی'

    def ready(self):
        import main.signals
