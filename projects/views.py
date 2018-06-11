from django.shortcuts import render, redirect
from .models import Project
from django.utils import timezone
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required


def home(request):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        projects = Project.objects.order_by("-pub_date")
        return render(request,'projects/projects_list.html',{'projects':projects})



def create(request):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        if request.method == 'POST':
            if request.POST['phone_Number'] and request.POST['address'] and request.POST['city'] and request.POST['state'] and request.POST['zip_Code'] and request.POST['building_Permit_Num'] and request.POST['plumbing_Permit_Num'] and request.POST['electric_Permit_Num'] and request.POST['zoning_Permit_Num'] and request.POST['mechanical_Permit_Num'] and request.POST['sign_Permit_Num']:
                project = Project()
                project.customer_Name = request.POST['customer_Name']
                project.phone_Number = request.POST['phone_Number']
                project.address = request.POST['address']
                project.city = request.POST['city']
                project.state = request.POST['state']
                project.zip_Code = request.POST['zip_Code']
                project.pub_date =timezone.datetime.now()
                project.building_Permit_Num = request.POST['building_Permit_Num']
                project.plumbing_Permit_Num = request.POST['plumbing_Permit_Num']
                project.electric_Permit_Num = request.POST['electric_Permit_Num']
                project.zoning_Permit_Num = request.POST['zoning_Permit_Num']
                project.mechanical_Permit_Num = request.POST['mechanical_Permit_Num']
                project.sign_Permit_Num = request.POST['sign_Permit_Num']
                project.save()
                return redirect('home')
            else:
                return redirect('home')


def get_project_info(request, id):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        project = get_object_or_404(Project, pk = id)
        return render(request, 'projects/project_info.html', {'project': project})


def edit_project(request,id):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        project = get_object_or_404(Project, pk = id)
        project.customer_Name = request.POST['customer_Name']
        project.phone_Number = request.POST['phone_Number']
        project.address = request.POST['address']
        project.city = request.POST['city']
        project.state = request.POST['state']
        project.zip_Code = request.POST['zip_Code']
        project.pub_date =timezone.datetime.now()
        project.building_Permit_Num = request.POST['building_Permit_Num']
        project.plumbing_Permit_Num = request.POST['plumbing_Permit_Num']
        project.electric_Permit_Num = request.POST['electric_Permit_Num']
        project.zoning_Permit_Num = request.POST['zoning_Permit_Num']
        project.mechanical_Permit_Num = request.POST['mechanical_Permit_Num']
        project.sign_Permit_Num = request.POST['sign_Permit_Num']
        project.save()
        return redirect('home')
