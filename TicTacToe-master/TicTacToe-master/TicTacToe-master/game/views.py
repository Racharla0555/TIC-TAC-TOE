from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.views import generic
name1=0
name2=0
def home(r):
    global name1,name2
    if r.method=='POST':
        name1=r.POST['name1']
        name2=r.POST['name2']
        level=r.POST['level']
        return redirect(f'/{level}')
    return render(r,'game/home.html')

def game(request, tiles):
    global name1,name2
    # Checking if no. of tiles is very high or low
    if tiles > 20 or tiles < 3:
        return HttpResponseBadRequest("<h1>No of tiles is not in bound [3,20]!")

    return render(request, 'game/game.html', {
        'tiles': tiles,
        'tiles_range': range(tiles),'player1':name1,'player2':name2
        })

