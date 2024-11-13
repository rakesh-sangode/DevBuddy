from pydoc_data import topics
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Room, Topic
from .forms import RoomForm

# rooms = [
#   {'id': 1, 'name': 'Lets learn Django'}, 
#   {'id': 2, 'name': 'Design with me'}, 
#   {'id': 3, 'name': 'Frontend Developer'}, 
# ]

def home(request):
  q = request.GET.get('q')
  rooms = Room.objects.filter(topic__name=q)
  topics = Topic.objects.all()
  context = {'rooms': rooms, 'topics': topics}   
  return render(request, "base/home.html", context)

def room(request, room_id):
  room = Room.objects.get(id=room_id)
  context = {'room': room}
  return render(request, "base/room.html", context)

def createRoom(request):
  form = RoomForm()
  if request.method == 'POST':
    form = RoomForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('home')
  context = {'form': form}
  return render(request, 'base/room_form.html', context)

def updateRoom(request, room_id):
  room = Room.objects.get(id=room_id)
  form = RoomForm(instance=room)
  if request.method == 'POST':
    form = RoomForm(request.POST, instance=room)
    if form.is_valid():
      form.save()
      return redirect('home')
  context = {'form': form}
  return render(request, 'base/room_form.html', context)

def deleteRoom(request, room_id):
  room = Room.objects.get(id=room_id)
  if request.method == 'POST':
    room.delete()
    return redirect('home')
  context = {'obj': room}
  return render(request, 'base/delete.html', context)
