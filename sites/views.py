from django.shortcuts import render
from django.views import View
from sites.models import Site, Detail
from django.db.models import Avg

class SitesView(View):
    template_name = 'sites/site-list.html'

    def get(self, request, *args, **kwargs):
        sites = Site.objects.all()
        return render(request, self.template_name, locals())


class SiteDetailsView(View):
    template_name = 'sites/site-details.html'

    def get(self, request, *args, **kwargs):
        try:
            site = Site.objects.get(pk=self.kwargs.get('site_id'))
        except Site.DoesNotExist:
            site = None
        details = Detail.objects.filter(site=site)
        return render(request, self.template_name, locals())


class SummaryView(View):
    template_name = 'sites/summary.html'

    def get(self, request, *args, **kwargs):
        sites = []

        # Only python implementation
        for site in Site.objects.all():
            A_value = sum([each.A_value for each in Detail.objects.filter(site=site)])
            B_value = sum([each.B_value for each in Detail.objects.filter(site=site)])
            sites.append({'name':site.name, 'A_value':A_value, 'B_value':B_value})

        return render(request, self.template_name, context={'sites':sites})


class SummaryAverageView(View):
    template_name = 'sites/summary_average.html'

    # Using Django DB API over SQL
    def get(self, request, *args, **kwargs):
        sites = Site.objects.all().annotate(A_value=Avg('detail_site__A_value'),
                                            B_value=Avg('detail_site__B_value'))
        return render(request, self.template_name, locals())
