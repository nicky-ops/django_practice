from django.urls import path, include
from . import views
from .views import EntryDetailView

urlpatterns = [
    path('weblog/', views.entries_index, name="entries_index"),
    path('weblog/<int:year>/<str:month>/<int:day>/<slug:slug>/', EntryDetailView.as_view(), name='entry-detail'),
]