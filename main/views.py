from django.shortcuts import render, get_object_or_404, redirect

from .models import DonorDB, NgoDB, ProjectDB, MilestonesDB, ContractDB, MilestoneReview


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


def moocow(request):
    moo = 'moo here'
    # t = MilestonesDB.objects.create(project_id=2, name ='Textbooks for Impoverished Kids in Africa', milestone_number = '1',  total_raise = '25000', current_raise = '20000', status='inprogress', extra1='Agong, Kenya', delivery_date='2018-11-15')
    # t.save

    context = {
        "moo": t,
        }
    return render(request, "home.html", context)
