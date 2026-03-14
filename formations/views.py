from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Formation
from .models import Session
from .models import Inscription
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from django.shortcuts import render
from comptes.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render


class FormationListView(ListView):
    model = Formation
    template_name = "formations/formation_list.html"
    context_object_name = "formations"


class FormationCreateView(CreateView):
    model = Formation
    fields = ['titre', 'description', 'duree', 'active']
    template_name = "formations/formation_form.html"
    success_url = reverse_lazy('formation_list')


class FormationUpdateView(UpdateView):
    model = Formation
    fields = ['titre', 'description', 'duree', 'active']
    template_name = "formations/formation_form.html"
    success_url = reverse_lazy('formation_list')


class FormationDeleteView(DeleteView):
    model = Formation
    template_name = "formations/formation_confirm_delete.html"
    success_url = reverse_lazy('formation_list')


from .models import Session


class SessionListView(ListView):
    model = Session
    template_name = "sessions/session_list.html"


class SessionCreateView(CreateView):
    model = Session
    fields = ['formation', 'date_debut', 'date_fin', 'capacite']
    template_name = "sessions/session_form.html"
    success_url = reverse_lazy('session_list')


class SessionUpdateView(UpdateView):
    model = Session
    fields = ['formation', 'date_debut', 'date_fin', 'capacite']
    template_name = "sessions/session_form.html"
    success_url = reverse_lazy('session_list')


class SessionDeleteView(DeleteView):
    model = Session
    template_name = "sessions/session_confirm_delete.html"
    success_url = reverse_lazy('session_list')



class InscriptionListView(ListView):
    model = Inscription
    template_name = "inscriptions/inscription_list.html"
    context_object_name = "inscriptions"

class InscriptionCreateView(CreateView):
    model = Inscription
    fields = ['employe', 'session']
    template_name = "inscriptions/inscription_form.html"
    success_url = reverse_lazy('inscription_list')

class InscriptionUpdateView(UpdateView):
    model = Inscription
    fields = ['progression', 'statut']
    template_name = "inscriptions/inscription_form.html"
    success_url = reverse_lazy('inscription_list')

class InscriptionDeleteView(DeleteView):
    model = Inscription
    template_name = "inscriptions/inscription_confirm_delete.html"
    success_url = reverse_lazy('inscription_list')


def generer_certificat(request, inscription_id):

    inscription = Inscription.objects.get(id=inscription_id)

    # vérifier si formation complétée
    if inscription.statut != "complete":
        return HttpResponse("La formation n'est pas encore complétée")

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="certificat.pdf"'

    p = canvas.Canvas(response)

    p.setFont("Helvetica-Bold", 20)
    p.drawString(200, 750, "Certificat de Formation")

    p.setFont("Helvetica", 14)

    p.drawString(100, 700, f"Employé : {inscription.employe.username}")
    p.drawString(100, 670, f"Formation : {inscription.session.formation.titre}")
    p.drawString(100, 640, f"Date Session : {inscription.session.date_debut}")

    p.drawString(100, 600, "Félicitations pour avoir complété cette formation.")

    p.save()

    return response




def is_rh(user):
    return user.role == 'RH'


@login_required
@user_passes_test(is_rh)
def dashboard_rh(request):

    total_formations = Formation.objects.count()
    total_sessions = Session.objects.count()
    total_inscriptions = Inscription.objects.count()

    total_employes = User.objects.filter(role='employe').count()

    context = {
        'formations': total_formations,
        'sessions': total_sessions,
        'inscriptions': total_inscriptions,
        'employes': total_employes,
    }

    return render(request, 'dashboard/dashboard_rh.html', context)

def home(request):
    return render(request, 'home.html')