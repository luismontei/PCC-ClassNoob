from django import forms
from django.shortcuts import render
from django.urls import reverse
from .models import PerguntasFrequentes, Duvida, Resposta
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect

class PerguntaFrequente(forms.ModelForm):

    class Meta:
        model = PerguntasFrequentes
        fields = ('titulo','descricao',)

class Duvidas(forms.ModelForm):

    class Meta:
        model = Duvida
        fields = ('titulo',)

class Respostas(forms.ModelForm):

    class Meta:
        model = Resposta
        fields = ('resposta',)