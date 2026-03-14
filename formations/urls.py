from django.urls import path
from .views import *

urlpatterns = [
    path('formations/', FormationListView.as_view(), name='formation_list'),
    path('formations/add/', FormationCreateView.as_view(), name='formation_add'),
    path('formations/<int:pk>/edit/', FormationUpdateView.as_view(), name='formation_edit'),
    path('formations/<int:pk>/delete/', FormationDeleteView.as_view(), name='formation_delete'),

    path('sessions/', SessionListView.as_view(), name='session_list'),
    path('sessions/add/', SessionCreateView.as_view(), name='session_add'),
    path('sessions/<int:pk>/edit/', SessionUpdateView.as_view(), name='session_edit'),
    path('sessions/<int:pk>/delete/', SessionDeleteView.as_view(), name='session_delete'),

    path('inscriptions/', InscriptionListView.as_view(), name='inscription_list'),
    path('inscriptions/add/', InscriptionCreateView.as_view(), name='inscription_add'),
    path('inscriptions/<int:pk>/edit/', InscriptionUpdateView.as_view(), name='inscription_edit'),
    path('inscriptions/<int:pk>/delete/', InscriptionDeleteView.as_view(), name='inscription_delete'),

    path('certificat/<int:inscription_id>/',generer_certificat,name='generer_certificat'),
    
    path('dashboard/', dashboard_rh, name='dashboard_rh'),
]