from . import views
from django.urls import path


urlpatterns = [
    path('', views.bag, name='bag'),
    path('add/<event_id>/', views.add_to_bag, name='add-to-bag'),
    path('remove/<event_id>/', views.remove_from_bag, name='remove-from-bag'),
]
