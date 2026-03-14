from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .forms import RegisterForm
from .models import User


# 🔹 Inscription utilisateur
def register(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('login')
    return render(request, 'accounts/register.html', {'form': form})


# 🔹 Redirection selon le rôle
def redirect_dashboard(request):
    if request.user.role == 'rh':
        return redirect('dashboard_rh')
    else:
        return redirect('dashboard_employe')


# ===============================
# CRUD EMPLOYES
# ===============================

# 📋 Liste des employés
class EmployeListView(ListView):
    model = User
    template_name = "accounts/employe_list.html"
    context_object_name = "employes"

    def get_queryset(self):
        return User.objects.filter(role='employe')


# ➕ Ajouter un employé
class EmployeCreateView(CreateView):
    model = User
    fields = ['username', 'email', 'password', 'role']
    template_name = "accounts/employe_form.html"
    success_url = reverse_lazy('employe_list')


# ✏ Modifier un employé
class EmployeUpdateView(UpdateView):
    model = User
    fields = ['username', 'email']
    template_name = "accounts/employe_form.html"
    success_url = reverse_lazy('employe_list')


# ❌ Supprimer un employé
class EmployeDeleteView(DeleteView):
    model = User
    template_name = "accounts/employe_confirm_delete.html"
    success_url = reverse_lazy('employe_list')