
from django.db import models
from django.contrib.auth.models import User
from django.forms import IntegerField
choix= (
('PC', 'Pouf en cuir'),
('OC', 'Oreillers en cuir'),
('TC', 'Têtes de lit en cuir'),
('SC', 'sac' ),

)
province_choices = (
('Chaouia-Ouardigha ' , 'Chaouia-Ouardigha '),
(' Doukkala-Abda ' , ' Doukkala-Abda '),
('Fès-Boulemane  ' , 'Fès-Boulemane  '),
(' Gharb-Chrarda-Beni Hssen ' , 'Gharb-Chrarda-Beni Hssen  '),
('Grand Casablanca  ' , ' Grand Casablanca '),
('Guelmim-Es Semara  ' , 'Guelmim-Es Semara  '),
('Laâyoune-Boujdour-Sakia el Hamra  ' , 'Laâyoune-Boujdour-Sakia el Hamra  '),
('Marrakech-Tensift-Al Haouz  ' , ' Marrakech-Tensift-Al Haouz '),
('Meknès-Tafilalet  ' , 'Meknès-Tafilalet  '),
('Oriental  ' , 'LOriental  '),
(' Oued ed Dahab-Lagouira ' , ' Oued ed Dahab-Lagouira '),
('Rabat-Salé-Zemmour-Zaër ' , 'Rabat-Salé-Zemmour-Zaër ') ,
('Souss-Massa-Drâa  ' , ' Souss-Massa-Drâa '), 
('Tadla-Azilal  ' , 'Tadla-Azilal  '),
('Tanger-Tétouan ' , 'Tanger-Tétouan ') ,
('Wilaya de Tanger ' , ' Wilaya de Tanger'),
(' Wilaya de Tétouan' , 'Wilaya de Tétouan '),
('Taza-Al Hoceïma-Taounate ' , 'Taza-Al Hoceïma-Taounate ') ,
)
stock= (
('disponible ' , 'disponible '),
(' Réapprovisionné ' , ' Réapprovisionné '),
('Quantités limitées  ' , 'Quantités limitées  '),
)
class Produit(models.Model):
    titre = models.CharField(max_length=100)
    prix_de_vente = models.FloatField()
    prix_réduit = models.FloatField()
    description = models.TextField()
    composition = models.TextField(default='')
    application_de_production = models.TextField(default='')
    categorie = models.CharField(choices=choix, max_length=2000)
    produit_image = models.ImageField(upload_to='produit')
    stock = models.CharField(choices=stock, max_length=2000)
    
    def __str__(self):
        return self.titre
class client (models.Model):
    utilisateur = models.ForeignKey(User,on_delete=models.CASCADE)
    nom = models.CharField (max_length=200)
    localisation = models.CharField(max_length=200)
    ville = models.CharField (max_length= 50)
    telephone = models.IntegerField()
    province = models.CharField(choices=province_choices, max_length=100)
def __str__(self):
        return self.name 

class panier (models.Model):

 utilisateur= models. ForeignKey (User, on_delete=models.CASCADE)
 produit = models.ForeignKey(Produit, on_delete=models.CASCADE)

 quantite = models. PositiveIntegerField(default=1)
@property
def totalmontant (self):
 return self.quantite*self.prix_de_vente
class favoris (models.Model):

 utilisateur= models. ForeignKey (User, on_delete=models.CASCADE)
 produit = models.ForeignKey(Produit, on_delete=models.CASCADE)

 quantite = models. PositiveIntegerField(default=1)

class adresse (models.Model):

 utilisateur= models. ForeignKey (User, on_delete=models.CASCADE)
 produit = models.ForeignKey(Produit, on_delete=models.CASCADE)

 quantite = models. PositiveIntegerField(default=1)
