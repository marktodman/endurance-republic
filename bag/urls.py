from . import views
from django.urls import path


urlpatterns = [
    path('', views.bag, name='bag'),
    path('add/<event_id>', views.add_to_bag, name='add-to-bag'),
]
