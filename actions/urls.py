from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.ActionList.as_view(), name='index'),
    url(r'^thismonth$', views.ActionsThisMonth.as_view(), name='thismonth'),
    url(r'^detail/(?P<pk>[0-9]+)$', views.ActionDetail.as_view(), name='detail'),
    url(r'^new$', views.new_action, name='new'),
    url(r'^edit/(?P<pk>[0-9]+)$', views.edit_action, name='edit'),
]
