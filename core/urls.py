from django.urls import path
from .views import registro, salvar, editar, update, delete, adm, login, agro, setor, adm2, adm3, adm4, adm5, adm6, registre

urlpatterns = [
    path('', agro, name='agro'),
    path('registro/', registro, name='registro'),
    path('salvar/', salvar, name='salvar'),
    path('editar/<int:id>', editar, name='editar'),
    path('update/<int:id>', update, name='update'),
    path('delete/<int:id>', delete, name='delete'),
    path('adm/', adm, name='adm'),
    path('login/', login, name='login'),
    path('setor/', setor, name='setor'),
    path('adm2/', adm2, name='adm2'),
    path('adm3/', adm3, name='adm3'),
    path('adm4/', adm4, name='adm4'),
    path('adm5/', adm5, name='adm5'),
    path('adm6/', adm6, name='adm6'),
    path('registre/', registre, name='registre'),
]
