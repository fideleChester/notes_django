from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
app_name = "notes"
urlpatterns = [
    path('', views.index, name="index"),
    path('eleves/', views.eleves, name="eleves"),
    path('eleve/<str:id>/', views.eleve, name="eleve"),
    path('niveau_pdf/<int:id_niveau>/', views.liste_niveauElv, name="niveau_pdf"),
    path('matieres/', views.matieres, name="matieres"),
    path('matiere/<int:id>/', views.matiere, name="matiere"),
    path('niveau/<int:id>/', views.niveau, name="niveau"),
    path('add_note/<str:eleve>/<int:matiere>/', views.add_note, name="add_note"),
    path("accounts/login/", auth_views.LoginView.as_view(template_name="registration/login.html")),
    path("viewPDF/",views.listEleves, name="viewPDF")

]

