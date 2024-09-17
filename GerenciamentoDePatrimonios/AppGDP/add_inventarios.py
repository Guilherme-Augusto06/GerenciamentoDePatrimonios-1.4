import os
import django
# Defina as configurações do Django para que o script funcione fora do ambiente Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "GerenciamentoDePatrimonios.settings")
django.setup()

# Agora fazemos uma importação absoluta, sem o "."
from AppGDP.models import Inventario  # Supondo que a app se chame Inventario

# Lista de inventários para adicionar
inventarios = [
    {"num_inventario": "789076", "denominacao": "ARMARIO BAIXO POST FORM. L-166 -02PB- CADERODE-", "localizacao": "20210066"},
    {"num_inventario": "789078", "denominacao": "ARMARIO BAIXO POST FORM. L-166 -02PB- CADERODE-", "localizacao": "20210066"},
    {"num_inventario": "775954", "denominacao": "CADEIRA FIXA C/4 PES - TECIDO AZUL ROYAL", "localizacao": "20210066"},
    {"num_inventario": "775959", "denominacao": "CADEIRA FIXA C/4 PES - TECIDO AZUL ROYAL", "localizacao": "20210066"},
    {"num_inventario": "775964", "denominacao": "CADEIRA FIXA C/4 PES - TECIDO AZUL ROYAL", "localizacao": "20210066"},
    {"num_inventario": "527070", "denominacao": "CADEIRA P/ SALA DE AULA DC 1307", "localizacao": "20210066"},
    {"num_inventario": "526155", "denominacao": "CADEIRA P/SALA DE AULA - DC 1307", "localizacao": "20210066"},

]

# Loop para adicionar cada item à tabela inventario
for item in inventarios:
    Inventario.objects.create(**item)

print("Todos os itens foram adicionados com sucesso!")
