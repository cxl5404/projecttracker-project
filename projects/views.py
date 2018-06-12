from django.shortcuts import render, redirect
from .models import Project
from django.utils import timezone
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required


def home(request):
        projects = Project.objects.order_by("-pub_date")
        return render(request,'projects/projects_list.html',{'projects':projects})



def create(request):
        if request.method == 'POST':
            if request.POST['phone_Number'] and request.POST['address'] and request.POST['city'] and request.POST['state'] and request.POST['zip_Code'] and request.POST['building_Permit_Num'] and request.POST['plumbing_Permit_Num'] and request.POST['electric_Permit_Num'] and request.POST['zoning_Permit_Num'] and request.POST['mechanical_Permit_Num'] and request.POST['sign_Permit_Num'] and request.POST['buildingplan'] and request.POST['plumbingplan'] and request.POST['electricalplan'] and request.POST['zoningplan'] and request.POST['signplan'] and request.POST['mechanicalplan']:
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
                project.Sign_Plan = request.POST['signplan']
                project.Building_Plan = request.POST['buildingplan']
                project.Mechanical_Plan = request.POST['mechanicalplan']
                project.Plumbing_Plan = request.POST['plumbingplan']
                project.Electric_Plan = request.POST['electricalplan']

                project.save()
                return redirect('home')
            else:
                return redirect('home')


def get_project_info(request, id):
        project = get_object_or_404(Project, pk = id)
        return render(request, 'projects/project_info.html', {'project': project})


def edit_project(request,id):
        project = get_object_or_404(Project, pk = id)
        project.customer_Name = request.POST['customer_Name']
        project.phone_Number = request.POST['phone_Number']
        project.address = request.POST['address']
        project.city = request.POST['city']
        project.state = request.POST['state']
        project.zip_Code = request.POST['zip_Code']
        project.pub_date =timezone.datetime.now()
        project.building_Permit_Num = request.POST['building_Permit_Num']
        project.BP_Status = request.POST['BP_Status']
        project.plumbing_Permit_Num = request.POST['plumbing_Permit_Num']
        project.PP_Status = request.POST['PP_Status']
        project.electric_Permit_Num = request.POST['electric_Permit_Num']
        project.EP_Status = request.POST['EP_Status']
        project.zoning_Permit_Num = request.POST['zoning_Permit_Num']
        project.ZP_Status = request.POST['ZP_Status']
        project.mechanical_Permit_Num = request.POST['mechanical_Permit_Num']
        project.MP_Status = request.POST['MP_Status']
        project.sign_Permit_Num = request.POST['sign_Permit_Num']
        project.SP_Status = request.POST['SP_Status']
        project.Zoning_Plan = request.POST['zplan']
        project.Sign_Plan = request.POST['splan']
        project.Building_Plan = request.POST['bplan']
        project.BP_Confirmation_Time = request.POST['ctime']
        project.Plumbing_Plan = request.POST['pplan']
        project.Mechanical_Plan = request.POST['mplan']
        project.Electric_Plan = request.POST['eplan']

        project.save()
        return redirect('home')

def search(request):
    address = request.GET.get('address', '')
    projects = Project.objects.filter(address__icontains=address)
    return render(request,'projects/search_list.html',{'projects':projects})
