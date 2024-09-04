from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2306165635',
        'name': 'Meutia Fajriyah',
        'class': 'PBP B'
    }

    return render(request, "main.html", context)
