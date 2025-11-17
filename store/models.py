from django.db import models

class MessageContact(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField()
    message= models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message[:30]



class DemandeDevis(models.Model):
    LOGEMENT_CHOICES = [
        ('Maison', 'Maison'),
        ('Studio', 'Studio'),
        ('1 pièce', '1 pièce'),
        ('2-3 pièces', '2-3 pièces'),
        ('Appartement', 'Appartement'),
    ]

    nom = models.CharField(max_length=100)
    email = models.EmailField()
    telephone = models.CharField(max_length=20)
    logement = models.CharField(max_length=20, choices=LOGEMENT_CHOICES)
    message = models.TextField(blank=True)
    date_demande = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nom} - {self.logement}"
