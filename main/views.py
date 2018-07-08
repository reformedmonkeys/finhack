from django.shortcuts import render, get_object_or_404, redirect

from .models import DonorDB, NgoDB, ProjectDB, MilestonesDB, ContractDB, MilestoneReview
from .forms import NewContract


# Create your views here.
def home(request):
    moo = 'moo here'
    context = {
        "moo": moo,
        }
    return render(request, "home.html", context)

def ngo(request, ngoID):

    owner = NgoDB.objects.filter(id=ngoID).latest('updated')
    ownerdid= owner.id
    queryset = ProjectDB.objects.filter(owner=ownerdid)

    moo = 'moo here'
    context = {
        "queryset": queryset,
        "owner": owner,
        }
    return render(request, "ngo.html", context)

def project(request, projectID):
    t = ProjectDB.objects.filter(id=projectID).latest('updated')
    ownerdid= t.owner.id
    owner = NgoDB.objects.filter(id=ownerdid).latest('updated')
    step = MilestonesDB.objects.filter(project=t.id)

    moo = 'moo here'
    context = {
        "t": t,
        "owner": owner,
        "step": step
        }
    return render(request, "project.html", context)


def donate(request, targetmilestone):
    t = MilestonesDB.objects.get(id=targetmilestone)
    towner = t.owner.id
    tproject=t.project.id
    t = ContractDB.objects.create(ngo_id=towner, project_id=tproject, milestone_id = targetmilestone, donor_id = 1, amount='200')
    t.save
    print "success"
    context = {
        "targetmilestone": targetmilestone,
        }
    return render(request, "donate2.html", context)


def mytrans(request, myid):
    t = ContractDB.objects.get(donor=myid)
    r = MilestoneReview.objects.get(donor=myid)
    name = DonorDB.objects.get(id=myid)
    context = {
        "t": t,
        "r": r,
        "name": "name"
        }
    return render(request, "mytrans.html", context)

def review_milestone(request, milestoneID):
    t = MilestoneReview.objects.get(id=milestoneID)
    print 'success'
    print targetmilestone
    context = {
        "targetmilestone": targetmilestone,
        }
    return render(request, "review.html", context)

def seeblockchain(request):
    t = ContractDB.objects.filter()
    r = MilestoneReview.objects.filter()

    context = {
        "t": t,
        "r": r,
        }
    return render(request, "mytrans.html", context)

def moocow(request):
    moo = 'moo here'
    # t = MilestonesDB.objects.create(project_id=2, name ='Textbooks for Impoverished Kids in Africa', milestone_number = '1',  total_raise = '25000', current_raise = '20000', status='inprogress', extra1='Agong, Kenya', delivery_date='2018-11-15')
    # t.save

    context = {
        "moo": t,
        }
    return render(request, "home.html", context)
