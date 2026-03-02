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

def Embaralhamento_dos_pacientes(lista_de_pacientes_original):
    lista_pacientes_embaralhada = lista_de_pacientes_original.copy() 
    random.shuffle(lista_pacientes_embaralhada)
    return lista_pacientes_embaralhada

pacientes_embaralhados = Embaralhamento_dos_pacientes(pacientes_da_semana)

print("Lista embaralhada:")
for paciente in pacientes_embaralhados:
    print(paciente)


def divisao_clientes_semana(lista_de_pacientes):
    pacientes_segunda = []
    pacientes_terca = []
    pacientes_quarta = []
    pacientes_quinta = []
    pacientes_sexta = []
    valor_divisao = len(lista_de_pacientes) // 5
    for i, paciente in enumerate(lista_de_pacientes):
        if i < valor_divisao:
            pacientes_segunda.append(paciente)
        elif valor_divisao <= i < 2 * valor_divisao:
            pacientes_terca.append(paciente)
        elif 2 * valor_divisao <= i < 3 * valor_divisao:
            pacientes_quarta.append(paciente)
        elif 3 * valor_divisao <= i < 4 * valor_divisao:
            pacientes_quinta.append(paciente)
        elif 4 * valor_divisao <= i < 5 * valor_divisao:
            pacientes_sexta.append(paciente)
    #print("Segunda-feira:", pacientes_segunda, "\n")
    #print("Terça-feira:", pacientes_terca, "\n")
    #print("Quarta-feira:", pacientes_quarta, "\n")
    #print("Quinta-feira:", pacientes_quinta, "\n")
    #print("Sexta-feira:", pacientes_sexta, "\n")

    return pacientes_segunda, pacientes_terca, pacientes_quarta, pacientes_quinta, pacientes_sexta

segunda, terca, quarta, quinta, sexta = divisao_clientes_semana(pacientes_embaralhados)