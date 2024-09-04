from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2306165742',
        'name': 'Bryan Mitch',
        'class': 'PBP A'
    }

    return render(request, "main.html", context)