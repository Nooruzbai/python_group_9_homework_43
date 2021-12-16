from django.urls import path

from webcalc.views import index_view

urlpatterns = [
    path('', index_view)
]