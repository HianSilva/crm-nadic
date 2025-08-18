from itertools import product

from django.contrib import admin
from django.contrib.messages import api
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('core.api.urls')),
    path('', include('core.urls')),
    path('api/accounts/', include('accounts.api.urls')),
]
