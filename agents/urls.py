from django.urls import path
from .views import AgentListView, AgentCreateList, AgentDetailView

app_name = 'agents'

urlpatterns = [
    path('', AgentListView.as_view(), name='main'),
    path('<int:pk>/', AgentDetailView.as_view(), name="detail"),
    # path('<int:pk>/update/', LeadUpdateView.as_view(), name="update"),
    # path('<int:pk>/delete/', LeadDeleteView.as_view(), name="delete"),
    path('create/', AgentCreateList.as_view(), name="create"),
]