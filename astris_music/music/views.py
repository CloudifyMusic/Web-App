from django.shortcuts import render

songs = [
    {
        'artist': 'Test1',
        'name': 'Test1'
    },
    {
        'artist': 'Test2',
        'name': 'Test2',
    },
    {
        'artist': 'Test3',
        'name': 'Test3',
    }

]

def home(request):
    context = {
        'songs': songs
    }
    return render(request, 'music/home.html', context)