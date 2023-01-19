from . import views
from django.urls import path


urlpatterns = [
    path('', views.EventList.as_view(), name='events'),
    path('admin_panel/', views.admin_panel, name='admin-panel'),
]