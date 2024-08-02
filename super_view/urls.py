from django.urls import path, include

from .views import List_view


urlpatterns = [
    path('List_view/', List_view.as_view(), name='List_view')
]