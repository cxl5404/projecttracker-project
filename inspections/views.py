from django.shortcuts import render

def inspections(request):
	return render(request,'inspections/inspections.html')