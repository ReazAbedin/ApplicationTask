from django.db import models

class Site(models.Model):
    name = models.CharField(verbose_name='Name', max_length=20)

    def __str__(self):
        return self.name


class Detail(models.Model):
    site = models.ForeignKey('sites.Site', models.CASCADE, related_name='detail_site')
    date = models.DateField(verbose_name='Date')
    A_value = models.FloatField(verbose_name='A Value')
    B_value = models.FloatField(verbose_name='B Value')

    def __str__(self):
        return self.site.name + '_' + self.date.strftime('%B_%d_%Y')