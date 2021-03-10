from django.contrib.gis import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('brew_base/', include('brew_base.urls')),
]
