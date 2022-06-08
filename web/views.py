from django.shortcuts import render, redirect
import web.models as models
# Create your views here.


def department_list(request):
    queryset = models.Department.objects.all()
    return render(request, 'department.html', {'queryset': queryset})


def department_add(request):
    if request.method == "GET":
        return render(request, 'department_add.html')

    title = request.POST.get("title")

    models.Department.objects.create(title=title)

    return redirect('/department/list/')


def department_delete(request):
    nid = request.GET.get("nid")
    models.Department.objects.filter(id=nid).delete()
    return redirect('/department/list/')


def department_edit(request, nid):
    if request.method == "GET":
        # get department title by nid
        row_obj = models.Department.objects.filter(id=nid).first()

        return render(request, 'department_edit.html', {"row_obj": row_obj})
    title = request.POST.get("title")
    models.Department.objects.filter(id=nid).update(title=title)

    return redirect('/department/list/')