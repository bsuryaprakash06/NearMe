from django.shortcuts import render

def map_view(request):
    return render(request, 'nyc.html')

def statue_view(request):
    return render(request, 'statue.html')

def empire_view(request):
    return render(request, 'empire.html')

def times_view(request):
    return render(request, 'times.html')

def park_view(request):
    return render(request, 'park.html')
