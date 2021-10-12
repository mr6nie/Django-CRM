from django.urls import path
from .views import LeadListView, LeadDeteilsView, LeadCreateView, LeadUpdateView, LeadDeleteView

app_name = "leads"

urlpatterns = [
    path('', LeadListView.as_view(), name="main"),
    path('<int:pk>/', LeadDeteilsView.as_view(), name="detail"),
    path('<int:pk>/update/', LeadUpdateView.as_view(), name="update"),
    path('<int:pk>/delete/', LeadDeleteView.as_view(), name="delete"),
    path('create/', LeadCreateView.as_view(), name="create"),
]