from django.shortcuts import render
from .models import StudentProfile,StudenInfo,StudentClass

def StudentsInformation(request,roll_no):
    std_add = StudentProfile.objects.get(std__roll=roll_no)
    context = {'profile':std_add}
    return render(request,'Student/studentDetail.html',context)

def StudentsImage(request,roll):
    std_pic = StudentProfile.objects.get(std__roll=roll)
    context = {'pro':std_pic}
    return render(request,'Student/imageDispaly.html',context)

def Class_wise_detail(request,cls):
    s_details = StudenInfo.objects.filter(std_class__name = cls)
    context = {'a':s_details}
    return render(request,'Student/class_wise_detail.html', context)







