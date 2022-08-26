from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from . models import Task
from . forms import  Tform
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView
class TodoListview(ListView):
    model = Task
    template_name = 'home.html'
    context_object_name = 'tasking'
class TodoDetailview(DetailView):
    model = Task
    template_name = 'details.html'
    context_object_name = 'task'
class TodoUpdateview(UpdateView):
    model =Task
    template_name='update.html'
    context_object_name = 'task'
    fields = ['name','priority','Date']
    def get_success_url(self):
        return reverse_lazy('detail',kwargs={'pk':self.object.id})
class TodoDeleteview(DeleteView):
    model =Task
    template_name='delete.html'
    success_url = reverse_lazy('Listview')

# Create your views here.
def task(request):
    tasking=Task.objects.all()
    if request.method=='POST':
        name=request.POST.get('task','')
        priority=request.POST.get('priority','')
        Date=request.POST.get('Date','')
        tasks=Task(name=name,priority=priority,Date=Date)
        tasks.save()
    return render(request,"home.html",{'tasking':tasking})
# def details(request):
#
#     return render(request,"details.html",)
def delete(request,taskid):
    taskd = Task.objects.get(id=taskid)
    if request.method=='POST':
        taskd.delete()
        return redirect('/')
    return render(request,'delete.html')
def update(request,id):
    tasku=Task.objects.get(id=id)
    form=Tform(request.POST or None,instance=tasku)
    if form.is_valid():
        form.save()
        return  redirect('/')
    return render(request,'edit.html',{'form':form,'tasku':tasku})

