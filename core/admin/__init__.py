from django.contrib import admin

from core.admin.pessoa import PessoaAdmin
from core.models import Pessoa

admin.site.register(Pessoa, PessoaAdmin)
