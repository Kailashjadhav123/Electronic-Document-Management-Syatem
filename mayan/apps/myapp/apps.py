from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _
from mayan.apps.common.apps import MayanAppConfig

class MyappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myapp'


class BackendsApp(MayanAppConfig):
    app_namespace = 'myapp'
    app_url = 'myapp'
    name = 'mayan.apps.myapp'
    verbose_name = _('myapp')