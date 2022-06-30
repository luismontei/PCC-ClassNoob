
from django.urls import path, include
from . import views

urlpatterns = [

    path('', views.home, name="home"), 
    path('addFaq/', views.addfaq, name="Adicionar-faq"),
    path('editfaq/<int:id_faq>', views.editfaq, name="Editar-Faq"),
    path('deletefaq/<int:id_faq>', views.deletefaq, name="Delete-Faq"),


    ################## Dúvidas ###################

    path('duvidas/', views.duvidas, name="View-Duvidas"),
    path('duvidas/', views.Search, name="Search"),
    path('duvidas/addDuvida/', views.addDuvida, name="Add-Duvida"),
    path('duvidas/minhasDuvidas/editDuvida/<int:id_duvida>', views.editDuvida, name='editDuvida'),
    path('duvidas/minhasDuvidas/delete/<int:id_duvida>', views.deletarDuvida, name='DeletarDuvida'),
    path('duvidas/minhasDuvidas/', views.minhasDuvidas, name='minhas duvidas'),

    ################# Respostas ##################

    path('duvidas/resposta/<int:id_resposta>', views.viewResposta, name="View-Resposta"),
    path('duvidas/responder/<int:id_resposta>', views.addResposta, name="add-Resposta"),
    path('duvidas/respostasAdmin/', views.respostaAdmin, name="edit-resposta"),
    path('duvidas/respostasAdmin/editResposta/<int:id_resposta>', views.editResposta, name="Edit-Resposta"),
    path('duvidas/respostasAdmin/deleteResposta/<int:id_resposta>', views.deleteResposta, name="delete-Respota"),
]
