from django.contrib import admin
from . models import Produit,client, panier,favoris,adresse

@admin.register(Produit)
class produiMdelAdmin(admin.ModelAdmin):
    list_display = ['id','titre','prix_de_vente','prix_réduit','stock','description', 'composition','application_de_production', 'categorie', 
 'produit_image',
            ]
@admin.register(client)
class clientMdelAdmin(admin.ModelAdmin):
    list_display = ['utilisateur', 'nom', 'localisation', 'ville', 'telephone', 'province']

 
@admin.register (panier)
class panierModelAdmin (admin.ModelAdmin):
  list_display=['id', 'utilisateur', 'produit', 'quantite']
  @admin.register (favoris)
  class favorisModelAdmin (admin.ModelAdmin):
   list_display=['id', 'utilisateur', 'produit']

   @admin.register (adresse)
   class adresseModelAdmin (admin.ModelAdmin):
    list_display=['id', 'utilisateur', 'produit', 'quantite']
