from django.urls import path, include
from .models import Entry
from . import views
from .views import EntryDetailView, ArchiveIndexView, YearArchiveView, MonthArchiveView, DayArchiveView, DateDetailView


entry_info_dict = {
    'queryset': Entry.objects.all(),
    'date_field': 'pub_date',
}
urlpatterns = [
    path('weblog/', views.entries_index, name="entries_index"),
    path('weblog/<int:year>/<str:month>/<int:day>/<slug:slug>/', EntryDetailView.as_view(), name='entry-detail'),
    path('weblog/', ArchiveIndexView.as_view(**entry_info_dict), name='archive_index'),
    path('weblog/<int:year>/', YearArchiveView.as_view(**entry_info_dict), name='archive_year'),
    path('weblog/<int:year>/<str:month>/', MonthArchiveView.as_view(**entry_info_dict), name='archive_month'),
    path('weblog/<int:year>/<str:month>/<int:day>/', DayArchiveView.as_view(**entry_info_dict), name='archive_day'),
    path('weblog/<int:year>/<str:month>/<int:day>/<slug:slug>/', DateDetailView.as_view(model=Entry, date_field='pub_date'), name='entry_detail'),
]