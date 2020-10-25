from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy, reverse
from .models import Todo
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from .forms import TodoCreationForm, TodoActiveForm, TodoUpdateForm
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class TodoListView(LoginRequiredMixin, generic.ListView):
    template_name = 'to_do/todo_list.html'
    context_object_name = 'what_to_do'

    def get_queryset(self):
        qs = Todo.undone.all().filter(owner=self.request.user)
        return qs

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['completed'] = Todo.done.all().filter(owner=self.request.user)
        return ctx

class TodoDetailView(LoginRequiredMixin, generic.UpdateView, generic.DetailView):
    model = Todo
    template_name = 'to_do/todo_detail.html'
    form_class = TodoActiveForm

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['active'] = self.get_form()
        return ctx

    def form_valid(self, form):
        self.object = self.get_object()
        if self.object.active == True:
            self.object.active = False
        else:
            self.object.active = True
        form.save()

        return redirect(reverse_lazy('to_do:todo_list'))
    
    def get_success_utl(self):
        return  reverse_lazy('to_do:todo_list')




class TodoCreateView(LoginRequiredMixin, generic.CreateView):
    form_class = TodoCreationForm
    template_name = 'to_do/create_todo.html'
    success_url = reverse_lazy('to_do:todo_list')
    
    def get_initial(self):
        initial = super().get_initial()
        initial['owner'] = self.request.user.id
        return initial

class TodoUpdateView(LoginRequiredMixin, generic.UpdateView):
    form_class = TodoUpdateForm
    queryset = Todo.undone.all()
    template_name = 'to_do/todo_update.html'
    success_url = reverse_lazy('to_do:todo_list')
