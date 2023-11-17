from django.urls import path
from . import views
app_name = "notes"
urlpatterns = [
    path('', views.index, name="index"),
    path('eleves/', views.eleves, name="eleves"),
    path('eleve/<int:id>/', views.eleve, name="eleve"),
    path('matieres/', views.matieres, name="matieres"),
    path('matiere/<int:id>/', views.matiere, name="matiere"),
    path('niveau/<int:id>/', views.niveau, name="niveau"),
    path('add_note/<int:eleve>/<int:matiere>/', views.add_note, name="add_note"),
]

