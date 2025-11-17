from django.shortcuts import render, redirect

from .forms import DemandeDevisForm
from .models import MessageContact

def home_view(request):
    return render(request, "home.html", {
        "title": "Bienvenue sur notre service de nettoyage",
        "description": "Professionnels du nettoyage d'appartements, bureaux et commerces."
    })

def contact_view(request):
    success = False
    if request.method == "POST":
        nom = request.POST.get("nom")
        email = request.POST.get("email")
        message = request.POST.get("message")
        MessageContact.objects.create(nom=nom, email=email, message=message)
        success = True
    return render(request, "servicenettoyage.html", {"success": success})

def detail_service_view(request):
    # Tu peux ajouter ici des informations dynamiques si besoin
    context = {
        "title": "Détails du service",
        "description": """ Nettoyage d’appartement

Nous proposons un nettoyage complet et structuré pour rendre votre appartement propre, sain et agréable à vivre.
Nos prestations incluent :

Dépoussiérage de toutes les surfaces

Lavage du sol

Nettoyage de la cuisine (plans de travail, plaques, évier…)

Entretien de la salle de bain et des toilettes

Nettoyage des vitres (option)

Désinfection des zones de contact

Un service idéal pour l’entretien régulier ou le nettoyage après un événement.
 Nettoyage d’une pièce / studio

Un service rapide et efficace pour les petits espaces :

Nettoyage du sol

Dépoussiérage du mobilier

Entretien rapide de la salle d’eau

Rafraîchissement de l’air et désinfection légère

Parfait pour les studios et les 1 pièce très fréquentés.

 Nettoyage de maison

Pour les logements plus grands, nous assurons un nettoyage complet de toutes les pièces :

Chambres

Salon

Cuisine complète

Sanitaires

Escaliers / terrasses selon demande

Ce service garantit un environnement propre et harmonieux dans toute la maison.

 Nettoyage avant emménagement / déménagement

Un service indispensable pour repartir sur une base propre :

Nettoyage en profondeur de toutes les pièces

Désinfection complète

Détartrage des sanitaires

Dépoussiérage des zones difficiles d’accès

Nettoyage cuisine + placards

Idéal pour remettre un logement à neuf avant de s’y installer ou le restituer propre.

 Nettoyage 2 à 3 pièces et plus

Adapté aux logements de taille moyenne ou familiale :

Nettoyage du sol dans toutes les pièces

Dépoussiérage approfondi

Traitement de la cuisine et salle de bain

Entretien balcon / couloir selon besoin

Un service flexible et efficace au meilleur rapport qualité/prix....""",
        "image": "static/images/img_net(1).jpg"  # exemple image
    }
    return render(request, "detail.html", context)

def about_view(request):
    context = {
        "title": "À propos de nous",
        "description": """
Nous sommes une entreprise spécialisée dans le nettoyage professionnel, dédiée à offrir des espaces propres, sains et agréables à vivre. 
Chez SNA Service, nous mettons notre expertise au service des particuliers comme des entreprises, en proposant des prestations complètes et adaptées à chaque besoin.

Notre équipe, sérieuse et expérimentée, intervient avec efficacité pour garantir un résultat impeccable, que ce soit pour le nettoyage de maisons, studios, appartements ou bureaux. 
Nous utilisons des produits et des techniques modernes, respectueux de l’environnement, afin d’assurer un entretien durable et de qualité.

Grâce à notre sens du détail, notre ponctualité et notre engagement envers la satisfaction client, nous sommes devenus un partenaire de confiance pour de nombreux foyers et professionnels.

Choisir SNA Service, c’est choisir la propreté, la tranquillité et un service sur mesure à Abidjan.
""",
        "image": "store/images/img_net_2.jpg"
    }
    return render(request, "about.html", context)
def demande_devis_view(request):
    success = False
    if request.method == "POST":
        form = DemandeDevisForm(request.POST)
        if form.is_valid():
            form.save()
            success = True
            form = DemandeDevisForm()  # vide le formulaire après envoi
    else:
        form = DemandeDevisForm()

    return render(request, "demande_devis.html", {"form": form, "success": success})