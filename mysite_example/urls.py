from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^actions/', include('actions.urls',namespace='actions')),
    url(r'^admin/', include(admin.site.urls)),
    
]
