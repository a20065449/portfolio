from django.contrib import admin

# Register your models here.
from .models import Cadeira, Pessoa, Projeto, Linguagem, PontuacaoQuizz, TrabalhoFC, Blog, Educacao, Questionario

admin.site.register(Cadeira)
admin.site.register(Pessoa)
admin.site.register(Projeto)
admin.site.register(Linguagem)
admin.site.register(PontuacaoQuizz)
admin.site.register(TrabalhoFC)
admin.site.register(Blog)
admin.site.register(Educacao)
admin.site.register(Questionario)

