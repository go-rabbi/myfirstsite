from django.shortcuts import render

# Create your views here.
def shortnerRes(request):
    return render(request,'urlshortner.html')