from django.db import models
from django.conf import settings

class Formation(models.Model):
    titre = models.CharField(max_length=200)
    description = models.TextField()
    duree = models.PositiveIntegerField(help_text="Durée en heures")
    date_creation = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.titre
    
    
class Session(models.Model):
    formation = models.ForeignKey(
        Formation,
        on_delete=models.CASCADE,
        related_name='sessions'
    )
    date_debut = models.DateField()
    date_fin = models.DateField()
    capacite = models.PositiveIntegerField()
    salle = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.formation.titre} ({self.date_debut})"

    def places_restantes(self):
        return self.capacite - self.inscriptions.count()
    
    
class Inscription(models.Model):
    STATUT_CHOICES = (
        ('en_cours', 'En cours'),
        ('complete', 'Complété'),
        ('abandon', 'Abandonné'),
    )

    employe = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        limit_choices_to={'role': 'employe'}
    )

    session = models.ForeignKey(
        Session,
        on_delete=models.CASCADE,
        related_name='inscriptions'
    )

    date_inscription = models.DateTimeField(auto_now_add=True)
    progression = models.PositiveIntegerField(default=0)
    statut = models.CharField(
        max_length=20,
        choices=STATUT_CHOICES,
        default='en_cours'
    )

    def __str__(self):
        return f"{self.employe.username} - {self.session}"
    
    class Meta:
        unique_together = ('employe', 'session')

    
class Certificat(models.Model):
    inscription = models.OneToOneField(
        Inscription,
        on_delete=models.CASCADE
    )
    date_generation = models.DateTimeField(auto_now_add=True)
    fichier = models.FileField(upload_to='certificats/', blank=True, null=True)

    def __str__(self):
        return f"Certificat - {self.inscription.employe.username}"