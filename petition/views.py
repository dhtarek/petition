from django.shortcuts import render
from .models import commune, petitions
from .models import domaine
# Create your views here.

def com_list(request):
    com_list = commune.objects.all()
    print(com_list)
    context = {'communes' :com_list}
    return render(request,'petition/commune_list.html', context)

def dom_list(request):
    dom_list = domaine.objects.all()
    context = {'domaines': dom_list}
    return render(request,'petition/domaine_list.html',context)


def commune_detail(request , id):
    commune_detail = commune.objects.get(id=id)   
    context = {'com': commune_detail}
    return render(request,'petition/commune_detail.html',context)