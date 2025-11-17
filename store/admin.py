from django.contrib import admin

from .models import MessageContact, DemandeDevis


class MessageContactAdmin(admin.ModelAdmin):
    list_display = ('nom', 'email', 'message', 'date')  # colonnes visibles
    search_fields = ('nom', 'email', 'message')         # barre de recherche
    list_filter = ('date',)                             # filtres par date
@admin.register(DemandeDevis)
class DemandeDevisAdmin(admin.ModelAdmin):
    list_display = ('nom', 'telephone', 'email', 'logement', 'date_demande')
    list_filter = ('logement', 'date_demande')
    search_fields = ('nom', 'email', 'telephone', 'message')

admin.site.register(MessageContact, MessageContactAdmin)