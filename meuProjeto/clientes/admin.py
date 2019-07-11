from django.contrib import admin
from .models import Cliente, Telefone, CPF, Departamento

admin.site.register(Cliente)
admin.site.register(Telefone)
admin.site.register(CPF)
admin.site.register(Departamento)
