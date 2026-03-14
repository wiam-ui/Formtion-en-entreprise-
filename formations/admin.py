from django.contrib import admin
from .models import Formation, Session, Inscription, Certificat

admin.site.register(Formation)
admin.site.register(Session)
admin.site.register(Inscription)
admin.site.register(Certificat)