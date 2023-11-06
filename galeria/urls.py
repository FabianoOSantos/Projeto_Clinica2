# Método Path, o PATCH é usado para atualização parcial, quando você não quer mandar o payload completo
#Conclusão: com a solicitação PATCH enviaríamos apenas os dados que precisamos modificar sem modificar ou afetar outras partes dos dados.

 # Importado da pasta > setup>Método Path""
from django.urls import path
#Importei dapasta urls>setup>urls)
from galeria.views import index


#Criar uma lista para manter todos os endpoints relacionado a galeria
urlpatterns = [
    path('', index)
]
