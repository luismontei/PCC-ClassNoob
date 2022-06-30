from django.contrib import admin

from .models import PerguntasFrequentes, Duvida, Resposta

admin.site.register(PerguntasFrequentes)
admin.site.register(Duvida)
admin.site.register(Resposta)