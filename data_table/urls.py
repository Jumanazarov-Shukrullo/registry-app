from django.urls import path

from data_table.views import index

urlpatterns = [
    path('', index, name='index')
]
