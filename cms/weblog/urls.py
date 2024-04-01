from django.urls import path, include
from weblog import views


urlpatterns = [
    path('weblog/', views.entries_index, name="entries_index"),
    path('weblog/<int:year>/<str:month>/<int:day>/<slug:slug>/', views.entry_detail, name='entry_detail')

]