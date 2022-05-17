from django.shortcuts import render


# Create your views here.
def webcam(request):
    context = {}
    return render(request, 'webcam/webcam.html', context=context)
