from django.apps import AppConfig
from suit.apps import DjangoSuitConfig


class FrontendConfig(AppConfig):
    name = 'frontend'

class SuitConfig(DjangoSuitConfig):
    layout: 'horizontal'


