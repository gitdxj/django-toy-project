from django.shortcuts import render

# Create your views here.


def department_list(request):
    return render(request, 'department.html')