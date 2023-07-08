from django.contrib import admin


class PessoaAdmin(admin.ModelAdmin):
    search_fields = ('nome',)
