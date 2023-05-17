from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from todotask.forms import TodoForms
from todotask.models import Task
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic.edit import UpdateView,DeleteView
class TaskDetailView(DetailView):
    model=Task
    template_name = 'taskdelete.html'
    context_object_name = 'task1'

class TaskListView(ListView):
    model = Task
    template_name = 'home.html'
    context_object_name = 'task'


class TaskUpdateView(UpdateView):
    model=Task
    template_name = 'update.html'
    context_object_name = 'task'
    fields= ('name','priority','date')

    def get_success_url(self):
        return reverse_lazy('cbvdetail',kwargs={'pk':self.object.id})


class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('cbvhome')



# Create your views here.
def add(request):
    task=Task.objects.all()
    if request.method=='POST':
        name=request.POST.get('taskname')
        priority=request.POST.get('priority')
        date=request.POST.get('date')
        Task.objects.create(name=name,priority=priority,date=date)


    return render(request,'home.html',{'task':task})

# def detail(request):
#     task=Task.objects.all()
#     return render(request,'taskdelete.html',{'task':task})

def delete(request,id):
    ta=Task.objects.get(id=id)
    if request.method=='POST':
        ta.delete()
        return redirect('/')
    return render(request,'delete.html')

def update(request,id):
    task=Task.objects.get(id=id)
    f=TodoForms(request.POST or None,instance=task)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(request,'edit.html',{'f':f,'task':task})
