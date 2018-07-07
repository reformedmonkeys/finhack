from django.shortcuts import render

# Create your views here.
def home(request):
    moo = 'moo here'
    context = {
        "moo": moo,
        }
    return render(request, "home.html", context)

def project_list(request):
    moo = 'moo here'
    context = {
        "moo": moo,
        }
    return render(request, "home.html", context)
