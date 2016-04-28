from django.shortcuts import render
from datetime import date
import calendar
from .models import Action
from .forms import ActionForm
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User

from django.views.generic import ListView, DetailView

class ActionList(ListView):
    model = Action
    queryset = Action.objects.order_by('-creation_date')
    context_object_name = 'data'
    template_name = 'actions/index.html'

class ActionsThisMonth(ListView):
    model = Action
    template_name = 'actions/index.html'
    context_object_name = 'data'
    
    def get_queryset(self):
        today = date.today()
        _, last_date = calendar.monthrange(today.year,today.month)
        start_date = date(year=today.year,month=today.month,day=1)
        end_date = date(year=today.year,month=today.month,day=last_date)
        return Action.objects.filter(creation_date__gte=start_date).filter(creation_date__lte=end_date)

class ActionDetail(DetailView):
   model = Action
   queryset = Action.objects.all()
   template_name = 'actions/detail.html'
   context_object_name = 'action'
    
# Forms to create, change, delete action
def new_action(request):
    if request.method == 'POST':
        form = ActionForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = User.objects.get(username=data['user'])
            new_action = Action(title=data['title'],
                                description=data['description'],
                                user=user)
            new_action.save()
            return HttpResponseRedirect('/actions')

    else:
        form = ActionForm()

    return render(request, 'actions/new.html', {'form': form})

def edit_action(request,pk):
    if request.method == 'POST':
        action = Action.objects.get(pk=pk)
        form = ActionForm(request.POST,instance=action)
        delete = request.POST.get('delete')
        if delete:
            action.delete()
        else:
            if form.is_valid():
                form.save()
        return HttpResponseRedirect('/actions')

    else:
        action = Action.objects.get(pk=pk)
        form = ActionForm(instance=action)

    return render(request, 'actions/edit.html', {'form': form,'pk':pk})
