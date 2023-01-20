from . import views
from django.urls import path


urlpatterns = [
    path('', views.EventList.as_view(), name='events'),
    path('admin_panel/', views.admin_panel, name='admin-panel'),
    path('edit_event/<event_id>', views.edit_event, name='edit-event'),
    path('add_event/', views.add_event, name='add-event'),
]
