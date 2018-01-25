from sites.views import SitesView, SiteDetailsView, SummaryView, SummaryAverageView
from django.urls import path

app_name = 'sites'

urlpatterns = [
    path(r'', SitesView.as_view(), name='Home'),
    path(r'sites/', SitesView.as_view(), name='site-list'),
    path(r'sites/<int:site_id>/', SiteDetailsView.as_view(), name='site_details'),
    path(r'summary/', SummaryView.as_view(), name='summary'),
    path(r'summary-average/', SummaryAverageView.as_view(), name='summary_average'),
]