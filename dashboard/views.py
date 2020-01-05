from django.shortcuts import render

def dashboardview(request):
    return render(request, 'dashboardview.html', {})

# Create your views here.
