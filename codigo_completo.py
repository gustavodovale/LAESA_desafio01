# Como será essa lógica:
# Objetivo a clinica deve atender todos os 40 pacientes, nos 5 dias da semana; 
# Com a primeira restrição de ser somente 8 pacientes por dia ;
# Com a segunda restrição de que especies tem ordem de prioridade começando com 
# Golfinhos -> Águias -> Leões -> ursos;
# Com a terceira restrição de que tem ordem de gravidade do paciente começando de 4, 3, 2, 1;
# Com a quarta restrição de que a prioridade de especie é superior a de gravidade;
# Com a quinta restrição de que no Minino 1 animal do tipo por dia;
## Primeiro vamos dividir os pacientes por dia da semana, depois vamos ordenar por especie e gravidade, e depois vamos aplicar as restrições de quantidade por dia, e quantidade de pacientes de gravidade 4 por dia. 
# Com a sexta restrição de que no Máximo 2 pacientes de gravidade 4 por dia;

import random

# os dados dos pacientes
pacientes_da_semana = [
{"id": 1, "especie": "Golfinho", "gravidade": 4},
{"id": 2, "especie": "Águia", "gravidade": 3},
{"id": 3, "especie": "Leão", "gravidade": 2},
{"id": 4, "especie": "Urso", "gravidade": 1},
{"id": 5, "especie": "Golfinho", "gravidade": 2},
{"id": 6, "especie": "Águia", "gravidade": 4},
{"id": 7, "especie": "Leão", "gravidade": 1},
{"id": 8, "especie": "Urso", "gravidade": 3},
{"id": 9, "especie": "Golfinho", "gravidade": 3},
{"id": 10, "especie": "Águia", "gravidade": 2},
{"id": 11, "especie": "Leão", "gravidade": 4},
{"id": 12, "especie": "Urso", "gravidade": 4},
{"id": 13, "especie": "Golfinho", "gravidade": 1},
{"id": 14, "especie": "Águia", "gravidade": 1},
{"id": 15, "especie": "Leão", "gravidade": 3},
{"id": 16, "especie": "Urso", "gravidade": 2},
{"id": 17, "especie": "Golfinho", "gravidade": 4},
{"id": 18, "especie": "Águia", "gravidade": 3},
{"id": 19, "especie": "Leão", "gravidade": 2},
{"id": 20, "especie": "Urso", "gravidade": 1},
{"id": 21, "especie": "Golfinho", "gravidade": 2},
{"id": 22, "especie": "Águia", "gravidade": 4},
{"id": 23, "especie": "Leão", "gravidade": 1},
{"id": 24, "especie": "Urso", "gravidade": 3},
{"id": 25, "especie": "Golfinho", "gravidade": 3},
{"id": 26, "especie": "Águia", "gravidade": 2},
{"id": 27, "especie": "Leão", "gravidade": 4},
{"id": 28, "especie": "Urso", "gravidade": 4},
{"id": 29, "especie": "Golfinho", "gravidade": 1},
{"id": 30, "especie": "Águia", "gravidade": 1},
{"id": 31, "especie": "Leão", "gravidade": 3},
{"id": 32, "especie": "Urso", "gravidade": 2},
{"id": 33, "especie": "Golfinho", "gravidade": 4},
{"id": 34, "especie": "Águia", "gravidade": 3},
{"id": 35, "especie": "Leão", "gravidade": 2},
{"id": 36, "especie": "Urso", "gravidade": 1},
{"id": 37, "especie": "Golfinho", "gravidade": 2},
{"id": 38, "especie": "Águia", "gravidade": 4},
{"id": 39, "especie": "Leão", "gravidade": 1},
{"id": 40, "especie": "Urso", "gravidade": 3}
]

# Função para embaralhar os pacientes
def Embaralhamento_dos_pacientes(lista_de_pacientes_original):
    lista_pacientes_embaralhada = lista_de_pacientes_original.copy() 
    random.shuffle(lista_pacientes_embaralhada)
    return lista_pacientes_embaralhada

pacientes_embaralhados = Embaralhamento_dos_pacientes(pacientes_da_semana)

#print("Lista embaralhada:")
#for paciente in pacientes_embaralhados:
#    print(paciente)

# Função para dividir os pacientes por dia da semana, respeitando as restrições
def divisao_clientes_semana(lista_de_pacientes):

    dias = {
        "segunda": [],
        "terca": [],
        "quarta": [],
        "quinta": [],
        "sexta": []
    }

    especies = ["Golfinho", "Águia", "Leão", "Urso"]

    # GARANTIR 1 DE CADA ESPÉCIE POR DIA
    for especie in especies:
        pacientes_da_especie = [p for p in lista_de_pacientes if p["especie"] == especie]
        #print(f"pacientes da especie {especie}: {pacientes_da_especie}")
        for dia in dias:
            paciente = pacientes_da_especie.pop()
            dias[dia].append(paciente)
            lista_de_pacientes.remove(paciente)

    # COMPLETAR ATÉ 8 POR DIA
    # RESPEITANDO NO MÁXIMO 2 DE GRAVIDADE 4
    for paciente in lista_de_pacientes:

        for dia in dias:

            if len(dias[dia]) >= 8:
                continue

            gravidade4_no_dia = sum(
                1 for p in dias[dia] if p["gravidade"] == 4
            )

            if paciente["gravidade"] == 4 and gravidade4_no_dia >= 2:
                continue

            dias[dia].append(paciente)
            break

    return dias

dias_da_semana = divisao_clientes_semana(pacientes_embaralhados)

# Imprimir os pacientes por dia da semana
for dia, lista in enumerate(dias_da_semana.items()):
    dia_nome, lista_pacientes = lista
    print(f"\n{dia_nome.capitalize()}:")
    for paciente in lista_pacientes:
        print(paciente)

# Função para ordenar os pacientes por espécie e gravidade
def prioridade_especie_gravidade(lista_dia, nome_dia):
    prioridade = {"Golfinho": 1, "Águia": 2, "Leão": 3, "Urso": 4}
    prioridade_gravidade = {4: 1, 3: 2, 2: 3, 1: 4}
    lista_ordenada = sorted(lista_dia, key=lambda x: (prioridade[x["especie"]], prioridade_gravidade[x["gravidade"]]))
    print(f"\nlista {nome_dia.capitalize()} ordenada por especie e gravidade: {lista_ordenada}\n")
    return lista_ordenada

segunda_feira_E_G_priorizado = prioridade_especie_gravidade(dias_da_semana["segunda"], "segunda")

terceira_feira_E_G_priorizado = prioridade_especie_gravidade(dias_da_semana["terca"], "terca")

quarta_feira_E_G_priorizado = prioridade_especie_gravidade(dias_da_semana["quarta"], "quarta")

quinta_feira_E_G_priorizado = prioridade_especie_gravidade(dias_da_semana["quinta"], "quinta")

sexta_feira_E_G_priorizado = prioridade_especie_gravidade(dias_da_semana["sexta"], "sexta")