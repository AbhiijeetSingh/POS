from django.shortcuts import render

def dashboardview(request):
    return render(request, 'dashboardview.html', {})

def about(request):
    return render(request, "about.html")

# Create your views here.
