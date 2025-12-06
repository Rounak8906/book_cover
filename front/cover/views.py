from django.shortcuts import render


def frontcover(request):
    return render(request, 'frontcover.html')