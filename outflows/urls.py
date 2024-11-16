from django.urls import path
from . import views

urlpatterns = [
    path('outflows/list/', views.OutflowListView.as_view(), name='outflow_list'),
    path('outflows/create/', views.OutflowCreateView.as_view(), name='outflow_create'),
    path('outflows/<int:pk>/detail/', views.OutflowDetailView.as_view(), name='outflow_detail'),

    path('api/v1/outflows/', views.OutflowListCreateAPIView.as_view(), name='outflow_list_create_api'),
    path('api/v1/outflows/<int:pk>/', views.OutflowRetrieveAPIView.as_view(), name='outflow_detail_api'),
]
