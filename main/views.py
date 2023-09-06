from django.shortcuts import render

# Create your views here.

def show_main(request):
    context = {
        'name': 'Neva Denstia Shabira',
        'class': 'PBP B'
    }

    return render(request, "main.html", context)
