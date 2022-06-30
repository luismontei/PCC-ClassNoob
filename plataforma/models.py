from django.db import models
from django.contrib.auth import get_user_model


########## - FAQ - ##########

#adicionar FAQ

class PerguntasFrequentes(models.Model):

    titulo = models.CharField(max_length=50)
    descricao = models.TextField()
    data_criacao = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.titulo)

class Duvida(models.Model):

    titulo = models.CharField(max_length=255)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    def __str__(self):
        return str(self.titulo)

class Resposta(models.Model):

    duvida_r = models.ForeignKey(Duvida, on_delete=models.CASCADE)
    resposta = models.CharField(max_length=255, blank=False)

    def __str__(self):
        return str(self.resposta)