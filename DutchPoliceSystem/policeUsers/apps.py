from django.apps import AppConfig

# Define APPS default auto field value
class PoliceUsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'policeUsers'
