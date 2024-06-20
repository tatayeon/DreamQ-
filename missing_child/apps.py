from django.apps import AppConfig


class MissingChildConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "missing_child"
