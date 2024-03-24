from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from home.models import Blog

class StaticSitemap(Sitemap):
    priority = 1.0
    changefreq = 'weekly'

    def items(self):
        return ['home', 'about', 'blogs', 'contact', 'faq', 'buy-book']
    
    
    def location(self, item):
        return reverse(item)

class BlogSitemap(Sitemap):
    priority = 1.0
    changefreq = 'daily'

    def items(self):
        return Blog.objects.all()

    def lastmod(self, obj):
        return obj.updated_at

    def location(self, obj):
        return f'/blog-post/{obj.slug}'