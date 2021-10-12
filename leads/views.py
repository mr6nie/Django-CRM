from django.shortcuts import render, redirect, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.core.mail import send_mail
from django.conf import settings

from .models import Lead, Agent
from .forms import LeadForm, CustomUserCreationForm

class SignupView(generic.CreateView):
    template_name = "registration/signup.html"
    form_class = CustomUserCreationForm

    def get_success_url(self):
        return reverse("login")

class LandingPageView(generic.TemplateView):
    template_name = "landing.html"

# lead list

class LeadListView(LoginRequiredMixin, generic.ListView):
    template_name = "leads/leads_list.html"
    queryset = Lead.objects.all()
    context_object_name = "leads"

# def leads_list(request):
#     lead = Lead.objects.all()
#     context = {
#         "leads": lead
#     }
#     return render(request, "leads/leads_list.html", context)

class LeadDeteilsView(LoginRequiredMixin, generic.DetailView):
    template_name = "leads/leads_details.html"
    queryset = Lead.objects.all()
    context_object_name = "lead"

# def lead_details(request, pk):
#     lead = Lead.objects.get(id=pk)
#     context = {
#         "lead": lead
#     }
#     return render(request, "leads/leads_details.html", context)

class LeadCreateView(LoginRequiredMixin, generic.CreateView):
    template_name = "leads/leads_create.html"
    form_class = LeadForm

    def get_success_url(self):
        return reverse('leads:main')

# ------------------------email sending---------------------------------------

    # def form_valid(self, form):
    #     send_mail(
    #         subject="A lead has been created",
    #         message=f"Go to the site to see new lead {Lead.first_name}",
    #         from_email = settings.DEFAULT_FROM_EMAIL,
    #         recipient_list=["mr.6nie@gmail.com"],
    #     )
    #     return super(LeadCreateView, self).form_valid(form)

# ------------------------email sending---------------------------------------

# def  lead_create(request):
#     form = LeadForm()
#     if request.method == "POST":
#         form = LeadForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/leads')
#     print(request.POST)
#     context = {
#         "form": LeadForm()
#     }
#     return render(request, "leads/leads_create.html", context)

class LeadUpdateView(LoginRequiredMixin, generic.UpdateView):
    template_name = "leads/leads_update.html"
    queryset = Lead.objects.all()
    form_class = LeadForm

    def get_success_url(self):
        return reverse('leads:main')

# def lead_update(request, pk):
#     lead = Lead.objects.get(id=pk)
#     form = LeadForm(instance=lead)
#     if request.method == "POST":
#         form = LeadForm(request.POST, instance=lead)
#         if form.is_valid():
#             form.save()
#             return redirect('/leads')
#     print(request.POST)
#     context = {
#         "form": form,
#         "lead": lead,
#     }
#     return render(request, "leads/leads_update.html", context)

class LeadDeleteView(LoginRequiredMixin, generic.DeleteView):
    template_name = "leads/leads_delete.html"
    queryset = Lead.objects.all()

    def get_success_url(self):
        return reverse('leads:main')

# def lead_delete(request, pk):
#     lead = Lead.objects.get(id=pk)
#     lead.delete()
#     return redirect('/leads')