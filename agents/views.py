from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import reverse
from leads.models import Agent
from .forms import AgentCreateForm

class AgentListView(LoginRequiredMixin, generic.ListView):
    template_name = 'agents/agent_list.html'
    queryset = Agent.objects.all()

class AgentCreateList(LoginRequiredMixin, generic.CreateView):
    template_name = "agents/agent_create.html"
    form_class = AgentCreateForm
    
    def get_success_url(self):
        return reverse("agents:main")

    def form_valid(self, form):
        agent = form.save()
        agent.save()
        return super(AgentCreateList, self).form_valid(form)

class AgentDetailView(LoginRequiredMixin, generic.DetailView):
    template_name = "agents/agent_detail.html"
    context_object_name = "agent"
    queryset = Agent.objects.all()

