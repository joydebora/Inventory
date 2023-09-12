from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        "inventory": "Petkeeper Inventory",
        "name": "Joy Debora Sitorus",
        "npm": "2206082991",
        "class": "PBP D",
    }

    return render(request, "main.html", context)