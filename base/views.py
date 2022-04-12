from django.shortcuts import render

# Create your views here.
rooms = [
    {'id': 1, 'name': 'Let us learn python'},
    {'id': 2, 'name': 'Java Developers'},
    {'id': 3, 'name': 'Database Admibns'},
]

def home(request):
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)

def room(request, pk):
    return render(request, 'base/room.html')

