from django.shortcuts import render
from .models import Division,District
# Create your views here.
def div_list(request):
    division_list = Division.objects.all()
    context = {'li':division_list}
    return render(request,'Info/division_list.html',context)

def distric_population_wise(request,name):
    dis = District.objects.filter(div__div_name=name,dis_population__gt=100)
    all = District.objects.all()
    context = {'di_name':dis,'all_dis':all}
    return render(request,'Info/district_population_wise.html',context)

def all_dis(request):
    all = District.objects.all()
    context = {'all_dis': all}
    return render(request, 'Info/all_district.html', context)

def population_order(request):
    pop_order = District.objects.order_by('-dis_population')
    context = {'population': pop_order}
    return render(request, 'Info/populations_order.html', context)