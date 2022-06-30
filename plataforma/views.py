from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib import messages
from .models import PerguntasFrequentes, Duvida, Resposta


from .forms import PerguntaFrequente, Duvidas, Respostas

def home(request):
    search = request.GET.get('search')

    if search:
        perguntas_frequentes = PerguntasFrequentes.objects.filter(titulo__icontains=search)
    else:
        perguntas_frequentes = PerguntasFrequentes.objects.all()

    context = {
        'pergunta_f': perguntas_frequentes
    }
    return render(request, 'plataforma/index.html', context)

def Search(request):
    search = request.GET.get('search')

    if search:
        duvidas = Duvida.objects.filter(titulo__icontains=search)
    else:
        duvidas = Duvida.objects.all()

    context = {
        'titulo': duvidas
    }
    return render(request, 'plataforma/duvida.html', context)


############## FAQ ###############


def addfaq(request):
    if request.method == 'POST':
        form = PerguntaFrequente(request.POST)
 
        if form.is_valid():
            pergunta_f = form.save(commit=False)
            pergunta_f.save()
            return redirect('/')
           
    else:
        form = PerguntaFrequente()
        return render(request, 'plataforma/admin_faq.html', {'form': form})

def editfaq(request, id_faq):
    pergunta_f = get_object_or_404(PerguntasFrequentes, pk=id_faq)
    form = PerguntaFrequente(instance=pergunta_f)
 
    if(request.method == 'POST'):
        form = PerguntaFrequente(request.POST, instance = pergunta_f)
 
        if(form.is_valid()):
            pergunta_f.save()
            return redirect('/')
        else:
            return render(request, 'plataforma/admin_faq.html', {'form':form})
 
    else:
        return render(request, 'plataforma/admin_faq.html', {'form':form})

def deletefaq(request, id_faq):
    pergunta_f = get_object_or_404(PerguntasFrequentes, pk=id_faq)
    pergunta_f.delete()
 
    return redirect('/')


############################## Duvida ###########################

#Visualizar
def duvidas(request):
    search = request.GET.get('search')
    if search:
        duvida = Duvida.objects.filter(titulo__icontains=search)
    else:
        duvida = Duvida.objects.all()

    context = {

        'duvida': duvida,

    }
    return render(request, 'plataforma/duvida.html', context)

#Adicionar


def addDuvida(request):
    if request.method == 'POST':
        form = Duvidas(request.POST)
 
        if form.is_valid():
            duvida = form.save(commit=False)
            duvida.user = request.user
            duvida.save()
            return redirect('/')
           
    else:
        form = Duvidas()
        return render(request, 'plataforma/addDuvida.html', {'form': form})

#Editar Dúvida

def editDuvida(request, id_duvida):
    titulo = get_object_or_404(Duvida, pk=id_duvida)
    form = Duvidas(instance=titulo)
 
    if(request.method == 'POST'):
        form = Duvidas(request.POST, instance = titulo)
 
        if(form.is_valid()):
            titulo.save()
            return redirect('/duvidas/minhasDuvidas/')
        else:
            return render(request, 'plataforma/editDuvida.html', {'form':form, 'titulo':titulo})
 
    else:
        return render(request, 'plataforma/editDuvida.html', {'form':form, 'titulo':titulo})

#Enviar Resposta


def viewResposta(request, id_resposta):
    duvida = get_object_or_404(Duvida, pk=id_resposta)
    respostas = Resposta.objects.all()

    context ={
        'duvida': duvida,
        'respostas': respostas,
    }
    return render(request, 'plataforma/visualizarRespostas.html', context)
#Deletar

def deletarDuvida(request, id_duvida):
    deleteD = get_object_or_404(Duvida, pk=id_duvida)
    deleteD.delete()
 
    return redirect('/duvidas/minhasDuvidas/')

#AdicionarResposta

def addResposta(request, id_resposta):
    duvida =  Duvida.objects.get(id=id_resposta)
    if request.method == 'POST':
        form = Respostas(request.POST)

        if form.is_valid():
            resposta = form.save(commit=False)
            resposta.duvida_r = duvida
            resposta.save()
            return redirect('/duvidas/')
    else: 
        form = Respostas()
        return render(request, 'plataforma/addResposta.html', {'form': form, 'duvida':duvida})


#Editar minhas respostas

def respostaAdmin(request):
    resposta = Resposta.objects.all()
    context = {
        'resposta': resposta,
    }
    return render(request, 'plataforma/adminRespostas.html', context)

#EditarResposta

def editResposta(request, id_resposta):
    resposta = get_object_or_404(Resposta, pk=id_resposta)
    form = Respostas(instance=resposta)
 
    if(request.method == 'POST'):
        form = Respostas(request.POST, instance = resposta)
 
        if(form.is_valid()):
            resposta.save()
            return redirect('/duvidas/')
        else:
            return render(request, 'plataforma/editResposta.html', {'form':form, 'resposta':resposta})
 
    else:
        return render(request, 'plataforma/editResposta.html', {'form':form, 'resposta':resposta})

def deleteResposta(request, id_resposta):
    delete = get_object_or_404(Resposta, pk=id_resposta)
    delete.delete()
    return redirect('respostasAdmin/')

def minhasDuvidas(request):
     duvida = Duvida.objects.filter(user=request.user)
     return render(request, 'plataforma/duvidasUsuario.html', {'duvida': duvida})