from multiprocessing import context
from django.shortcuts import render

from internship.models import Company

# Create your views here.

def home(request):

    context = {}
    return render(request, 'internship/home.html', context)

def interns(request):
    comp = Company.objects.all()

    context = { 'comp': comp }
    return render(request, 'internship/interns.html', context)

def company(request):

    if request.method == 'POST':
        if request.POST.get('save'):
            comp_name = request.POST.get('comp_name')
            comp_about = request.POST.get('comp_about')
            comp_location = request.POST.get('comp_location')
            comp_digi_address = request.POST.get('comp_digi_address')
            comp_role = request.POST.get('comp_role')
            addi_info = request.POST.get('comp_addi_info')
        
            
            
            # check name, digital adress

            c = Company(name=comp_name, about=comp_about)
            c.save()
            c.location_set.create(name=comp_location, digi_address=comp_digi_address)
            c.companyrole_set.create(name=comp_role, addi_info=addi_info)


    context = {}
    return render(request, 'internship/company.html', context)

def processApplication(request, id):
    comp = Company.objects.get(id=id)
    ls = comp.location_set.all()
    rs = comp.companyrole_set.all()
    context = {'location_set': ls, 'role_set': rs}
    return render(request, 'internship/interns.html', context)

# def login