from django.shortcuts import render
from django.http import HttpResponse
import spotipy
sp = spotipy.Spotify()

def index(request):
    return render(request, 'queue/index.html')

def add(request):
    return render(request, 'queue/add.html')

def vote(request):
    return render(request, 'queue/vote.html')

def playlist(request):
	x = request.POST.get('artist', False)
	print(x)
	allSongsofArtist(x)
	return render(request, 'queue/playlist.html')


def allSongsofArtist (artist):
	results = sp.search(q=artist, limit=10)
	for i, t in enumerate(results['tracks']['items']):
	    print(' ', i, t['name'])