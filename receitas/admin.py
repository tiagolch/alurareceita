from django.contrib import admin
from .models import Receita


class ListandoReceitas(admin.ModelAdmin):
    list_display = ('id', 'nome_receita', 'tempo_preparo', 'rendimento', 'date_receita', 'publicada')
    list_display_links = ('id', 'nome_receita')
    list_editable = ('tempo_preparo','publicada',)
    search_fields = ('nome_receita',)
    list_filter = ('categoria',)
    list_per_page = 4


admin.site.register(Receita, ListandoReceitas)




