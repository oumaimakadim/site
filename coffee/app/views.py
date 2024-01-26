
from django.db.models import Count
from django.shortcuts import render, redirect
from django.views import View
from . models import Produit
from .forms import CustomerRegistrationForm,CustomerProfileForm
from . models import panier, client , Produit
from django.contrib import messages
# Create your views here.
def page_paiement_carte(request):
    return render(request,"app/page_paiement_carte.html") 

def favoris(request):
    return render(request,"app/favoris.html") 
def accueil(request):
    return render(request,"app/accueil.html")
def index(request):
    return render(request,"app/index.html") 

def apropos(request):
    return render(request,"app/apropos.html")
def panier(request):
    return render(request,"app/panier.html")

def contact(request):
    return render(request,"app/contact.html")
def Q2(request):
    return render(request,"app/Q2.html")
def Q3(request):
    return render(request,"app/Q3.html")
def Q4(request):
    return render(request,"app/Q4.html")
def profile(request):
    return render(request,"app/profile.html")

def ajouterau_panier(request):
    utilisateur = request.user
    produit_id = request.GET.get('prod_id')
    produit = Produit.objects.get(id=produit_id)
    panier_items = panier(utilisateur=utilisateur, produit=produit)
    panier_items.save()
    return redirect("/panier")

            
def voir_panier(request):
                user = request.user 
                paniers = panier.objects.filter(utilisateur=user)
                return render (request , "app/ajouteraupanier.html",locals())

class CategorieView(View):
    def get (self,request,val):
        produit = Produit.objects.filter(categorie=val)
        titre = Produit.objects.filter(categorie=val).values('titre')
        return render(request,"app/categorie.html",locals())

class CategorieTitre(View):
    def get (self,request,val):
        produit = Produit.objects.filter(titre=val)
        titre = Produit.objects.filter(categorie=produit[0].categorie).values('titre')
        return render(request,"app/categorie.html",locals())


class detailProduit(View):
    def get (self,request,pk):
        produit = Produit.objects.get(pk=pk)
        return render (request,"app/detailProduit.html",locals())

from django.contrib import messages

class CustomerRegistrationView(View):
    def get(self, request):
        form = CustomerRegistrationForm()
        return render(request, 'app/customerregistration.html', locals())

    def post(self, request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Congratulations!")
        else:
            messages.warning(request, "Invalid input data")
        return render(request, 'app/customerregistration.html', locals())
    

    class ProfileView(View):
     def get(self, request):
        form = CustomerProfileForm()
        return render(request, 'app/profile.html', locals())
    
    def post(self, request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            user = request.user
            nom = form.cleaned_data['nom']
            localisation = form.cleaned_data['localisation']
            ville = form.cleaned_data['ville']
            telephone = form.cleaned_data['telephone']
            province = form.cleaned_data['province']
            
            # Enregistrer les données dans le modèle client
            client_obj = client(user=user, nom=nom, localisation=localisation, ville=ville, telephone=telephone, province=province)
            client_obj.save()
        return render(request, 'app/profile.html', locals())