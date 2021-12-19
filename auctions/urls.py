from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("register/", views.register, name="register"),
    path("create_list/",views.create_list, name="create_list"),
    path("listing_page/<int:id>/",views.listing_page, name="listing_page"),
    path("add_to_watchlist/<int:id>/",views.add_to_watchlist,name="add_to_watchlist"),
    path("remove_from_watchlist/<int:id>/",views.remove_from_watchlist,name="remove_from_watchlist"),
    path("watchlist/",views.watchlist_view,name="watchlist"),
    path("add_bid/",views.add_bid, name="add_bid"),
    path("bid_history/<int:id>/",views.bid_history, name="bid_history"),
    path("close_auction/<int:id>/",views.close_auction,name="close_auction"),
    path("add_comment/<int:id>/",views.add_comment, name="add_comment"),
    path('categories/<str:category>/',views.categories_view,name="categories"),
    path('my_listing/',views.my_listing_view, name='my_listing')
]
