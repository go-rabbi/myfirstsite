from django.shortcuts import render
import uuid
from .models import URL
from django.http import HttpResponse


# Create your views here.
def shortnerRes(request):
    return render(request,'urlshortner.html')

def create(request): 
    if request.method=='POST':
        link=request.POST['link']
        uid=str(uuid.uuid4())[:5]
        new_url=URL(link=link,uuid=uid)
        new_url.save()
        return HttpResponse(uid)
        