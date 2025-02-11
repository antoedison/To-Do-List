from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from .models import Details
from django.utils.timezone import make_aware
# Create your views here.

def dashboard(request):
    #return HttpResponse("This Page shows the tasks")
    return render(request,'dashboard.html')

def add_task(request):
    
    if request.method == 'POST':
        task_name = request.POST.get("task_name")
        task_desc = request.POST.get("task_desc")
        task_status = request.POST.get("task_status", False)
        #deadline = request.POST.get("task_deadline")
        if Details.objects.filter(task_name=task_name).exists():
            return render(request, 'add_task.html', {'error': 'Task with this name already exists'})
        """
        if deadline:
                try:
                    deadline_dt = make_aware(deadline.datetime.strptime(deadline, "%Y-%m-%dT%H:%M"))
                except ValueError:
                    return render(request, 'add_task.html', {'error': 'Invalid date format'})
        """
        Details.objects.create(task_name= task_name, task_desc = task_desc, task_status = task_status)
        return redirect('view_task')
    details = Details.objects.all()
    return render(request,'add_task.html',{'details': details})

def view_task(request):
    task = Details.objects.all()
    return render(request, 'view_task.html', {'details': task})

def completed_task(request):
    task = Details.objects.filter(task_status = True)
    return render(request, 'completed_task.html', {'details': task})

def edit_task(request):
    return render(request, 'edit_task.html')
