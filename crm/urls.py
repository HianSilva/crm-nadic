from itertools import product

from django.contrib import admin
from django.contrib.messages import api
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(('core.api.urls', 'core'), namespace='crm-api')),
    path('', include(('core.urls', 'core'), namespace='crm')),
    path('api/accounts/', include(('accounts.api.urls', 'accounts'), namespace='accounts-api')),
]
