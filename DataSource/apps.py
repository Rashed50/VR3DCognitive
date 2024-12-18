from django.apps import AppConfig


class DatasourceConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'DataSource'

    def ready(self):
        import DataSource.signals
