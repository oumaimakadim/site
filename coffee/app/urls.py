from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_view 
from .forms import LoginForm, MyPasswordResetForm
urlpatterns = [
    path("", views.accueil),
   
    path('page_paiement_carte/',views.page_paiement_carte,name="page_paiement_carte"),
     path('favoris/',views.favoris,name="favoris"),
    path('panier/',views.panier,name="panier"),
    path('Q2/',views.Q2,name="Q2"),
     path('Q3/',views.Q3,name="Q3"),
      path('Q4/',views.Q4,name="Q4"),
    path('apropos/',views.apropos,name="apropos"),
    path('contact/',views.contact,name="contact"),
    path('index/',views.index,name="index"),
    path("categorie/<slug:val>", views.CategorieView.as_view(), name='categorie'),
    path("categorie-titre/<val>",  views.CategorieTitre.as_view(), name='categorie-titre'),
    path(" detailProduit/<int:pk>", views.detailProduit.as_view(), name='detailsProduit'),

path('ajouterau_panier/', views.ajouterau_panier, name='ajouterau_panier'),
path('panier /', views. voir_panier, name='voir_panier'),
path('verifier/', views. voir_panier, name='verifier'),


path ('registrations',views.CustomerRegistrationView.as_view(),name='custumerregistration'),
path('accounts/login/',auth_view.LoginView.as_view (template_name = 'app/login.html',authentication_form=LoginForm ),name = 'login'),
path('password_reset/',auth_view.PasswordResetView.as_view (template_name = 'app/passwordr.html',form_class = MyPasswordResetForm),name = 'password_reset'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

