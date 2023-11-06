from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('eleves/', views.eleves, name="eleves"),
    path('eleve/<int:id>/', views.eleve, name="eleve"),
    path('matieres/', views.matieres, name="matiere"),
    path('matiere/<int:id>/', views.matiere, name="matiere"),
    path('niveau/<int:id>/', views.niveau, name="niveau"),
]

