from django.shortcuts import render, redirect
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from .models import Event, Venue
from .forms import VenueForm, EventForm
from django.http import HttpResponseRedirect

# Create your views here.
def add_event(request):
    submitted = False
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add-event?submitted=True')
    else:
        form = EventForm
        if 'submitted' in request.GET:
            submitted = True
        
    return render(request, 'events/add-event.html', {'form': form, 'submitted':submitted})

def update_venue(request, venue_id):
    venue = Venue.objects.get(pk=venue_id)
    form = VenueForm(request.POST or None, instance=venue)
    if form.is_valid():
        form.save()
        return redirect('venue_list')
        
    return render(request, 'events/update-venue.html', {'venue': venue, 'form': form})


def update_event(request, event_id):
    event = Event.objects.get(pk=event_id)
    form = EventForm(request.POST or None, instance=event)
    if form.is_valid():
        form.save()
        return redirect('events_list')
        
    return render(request, 'events/update-event.html', {'event': event, 'form': form})


def search_venue(request):     
    if request.method == "POST":
        searched = request.POST['searched']
        venues = Venue.objects.filter(name__contains=searched)
        return render(request, 'events/search-venue.html', {'searched': searched, 'venues': venues})
    else:
        return render(request, 'events/search-venue.html')


def venue_list(request):
    venue_list = Venue.objects.all()
    return render(request, 'events/venue-list.html', {'venue_list': venue_list})


def events_list(request):
    event_list = Event.objects.all().order_by('?')
    return render(request, 'events/event-list.html', {'event_list': event_list})


def show_venue(request, venue_id):
    venue = Venue.objects.get(pk=venue_id)
    return render(request, 'events/show-venue.html', {'venue': venue})


def home(request, year=datetime.now().year, month=datetime.now().strftime('%B')):
    name = "Fuck"
    month = month.capitalize()
    month_number = list(calendar.month_name).index(month)
    month_number = int(month_number)
    
    cal = HTMLCalendar().formatmonth(year, month_number)
    now = datetime.now()
    current_year = now.year
    time = now.strftime('%H:%M')
    
    return render(request, "events/home.html", {
        'name': name,
        'year': year,
        'month': month,
        'month_number': month_number,
        "cal": cal,
        "now": now,
        "this_year": current_year,
        'time': time
    })


def add_venue(request):
    submitted = False
    if request.method == "POST":
        form = VenueForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add-venue?submitted=True')
    else:
        form = VenueForm
        if 'submitted' in request.GET:
            submitted = True
        
    return render(request, 'events/add-venue.html', {'form': form, 'submitted':submitted})


def delete_event(request, event_id):
    event = Event.objects.get(pk=event_id)
    event.delete()
    return redirect('events_list')


def delete_venue(request, venue_id):
    venue = Venue.objects.get(pk=venue_id)
    venue.delete()
    return redirect('venue_list')