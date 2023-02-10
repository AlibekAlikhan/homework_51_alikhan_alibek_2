from django.urls import path

from webapp.views.articles import add_view

from webapp.views.articles import cat_stats

urlpatterns =[
    path('', add_view),
    path('cat_stats', cat_stats),
]
