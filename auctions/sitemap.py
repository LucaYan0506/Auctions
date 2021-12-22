from django.contrib.admin.sites import site
from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from .models import categories,Auction

class StaticViewSitemap(Sitemap):

    def items(self):
        return [
            'index',
            'login',
            'logout',
            'register',
            'create_list',
            'watchlist',
            'add_bid',
            'my_listing',
        ]

    def location(self,item):
        return reverse(item)

class CategorieViewSitemap(Sitemap):
    
    def items(self):
        return categories.objects.all()


class Listing_pageViewSitemap(Sitemap):
    
    def items(self):
        return Auction.objects.all()