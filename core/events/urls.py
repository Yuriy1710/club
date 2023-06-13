from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('<int:year>/<str:month>/', views.home, name="home"),
    path('events/', views.events_list, name="events_list"),
    path('add-venue', views.add_venue, name="add_venue"),
    path('venue-list/', views.venue_list, name="venue_list"),
    path('show-venue/<venue_id>', views.show_venue, name="show_venue"),
    path('search-venue/', views.search_venue, name="search_venue"),
    path('update-venue/<venue_id>', views.update_venue, name="update_venue"),
    path('add-event', views.add_event, name="add_event"),
    path('update-event/<event_id>', views.update_event, name="update_event"),
    path('delete-event/<event_id>', views.delete_event, name="delete_event"),
    path('delete-venue/<venue_id>', views.delete_venue, name="delete_venue"),
]
