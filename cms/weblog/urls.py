from django.urls import path, include
from weblog import views


urlpatterns = [
    path('weblog/', views.entries_index, name="entries_index"),
    path(r'^weblog/(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$', views.entry_detail, name="entries_detail"),
]