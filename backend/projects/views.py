from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .models import Project, Skill
from .forms import ProjectForm

def index(request):
    projects = Project.objects.all()
    skills = Skill.objects.all()
    
    active_skill = request.GET.get('skill')
    if active_skill:
        projects = projects.filter(required_skills__name=active_skill)
    
    context = {
        'projects': projects,
        'skills': skills,
        'active_skill': active_skill
    }
    return render(request, 'projects/index.html', context)

class ProjectCreate(LoginRequiredMixin, CreateView):
    model = Project
    form_class = ProjectForm
    template_name = 'projects/project_form.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class ProjectDetail(DetailView):
    model = Project
    template_name = 'projects/project_detail.html'

@login_required
def join_project(request, pk):
    project = get_object_or_404(Project, pk=pk)
    
    if project.author != request.user:
        if request.user in project.participants.all():
            project.participants.remove(request.user)
        else:
            project.participants.add(request.user)
            
    return redirect('projects:detail', pk=pk)


class ProjectUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Project
    form_class = ProjectForm
    template_name = 'projects/project_form.html'
    success_url = reverse_lazy('index')
    
    def test_func(self):
        project = self.get_object()
        return self.request.user == project.author

class ProjectDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Project
    template_name = 'projects/project_confirm_delete.html'
    success_url = reverse_lazy('index')

    def test_func(self):
        project = self.get_object()
        return self.request.user == project.author