from django.shortcuts import render

from ground0.models import Artist

# Create your views here.
def index(request):
    latest_artist_list = Artist.objects.order_by('-dateTime')[:5]
    context = {'latest_artist_list': latest_artist_list}

    return render(request, 'ground0/index.html', context)
