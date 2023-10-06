from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .forms import TodoForm
from .models import Task
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView


class Tasklistview(ListView):
    model = Task
    template_name = 'home1.html'
    context_object_name = 'task1'
    fields = ('name', 'priority', 'date')


class Tastdetailview(DetailView):
    model = Task
    template_name = 'details.html'
    context_object_name = 'task'



class Taskupdateview(UpdateView):
    model = Task
    template_name = 'edit.html'
    context_object_name = 'task'
    fields = ('name', 'priority', 'date')
    success_url = reverse_lazy('todoapp:cbvhome')

    # def get_success_url(self):
    #     return reverse_lazy('todoapp:details', kwargs={'pk': self.object.id})

class Taskdeleteview(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('todoapp:cbvhome')

# Create your views here.

def add(request):
    task1 = Task.objects.all()
    if request.method == 'POST':
        name = request.POST.get('task', '')
        priority = request.POST.get('priority', '')
        date = request.POST.get('date', '')
        task = Task(name=name, priority=priority, date=date)
        task.save()
    return render(request, 'home.html', {'task1': task1})


# def details(request):
#     task = Task.objects.all()
#     return render(request, 'details.html', {'task': task})

def delete(request, taskid):
    task = Task.objects.get(id=taskid)
    if request.method == 'POST':
        task.delete()
        return redirect('/')
    return render(request, 'delete.html')


def update(request, id):
    task = Task.objects.get(id=id)
    f = TodoForm(request.POST or None, instance=task)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(request, 'update.html', {'f': f, 'task': task})
