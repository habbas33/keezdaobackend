from django.shortcuts import render

def gethome(request):
    return render(request, 'index.html', {})