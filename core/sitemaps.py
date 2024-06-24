from django.contrib.sitemaps import Sitemap
from .models import Index_Section

class TNWebSitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.5

    def items(self):
        return Index_Section.objects.filter(page_name='index')

    def lastmod(self, obj):
        return obj.updated_at
