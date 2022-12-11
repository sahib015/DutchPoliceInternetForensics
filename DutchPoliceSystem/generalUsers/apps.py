from django.apps import AppConfig

# Define APPS default auto field value
class GeneralusersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'generalUsers'
