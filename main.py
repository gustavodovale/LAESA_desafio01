# Como será essa lógica:
# Objetivo a clinica deve atender todos os 40 pacientes, nos 5 dias da semana; 
# Com a primeira restrição de ser somente 8 pacientes por dia ;
# Com a segunda restrição de que especies tem ordem de prioridade começando com 
# Golfinhos -> Águias -> Leões -> ursos;
# Com a terceira restrição de que tem ordem de gravidade do paciente começando de 4, 3, 2, 1;
# Com a quarta restrição de que a prioridade de especie é superior a de gravidade;
# Com a quinta restrição de que no Minino 1 animal do tipo por dia;
# Com a sexta restrição de que no Máximo 2 pacientes de gravidade 4 por dia;


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

def maximo_clientes_dia(lista_de_pacientes):
    lista_do_Dia = []
    for paciente in lista_de_pacientes:  # Considerando apenas os primeiros 8 pacientes como um dia
        lista_do_Dia.append(paciente)
    print(lista_do_Dia)

# maximo_clientes_dia(pacientes_da_semana)

def divisao_clientes_semana(lista_de_pacientes):
    pacientes_segunda = []
    pacientes_terca = []
    pacientes_quarta = []
    pacientes_quinta = []
    pacientes_sexta = []
    for i, paciente in enumerate(lista_de_pacientes):
        if i < 8:
            pacientes_segunda.append(paciente)
        elif 8 <= i < 16:
            pacientes_terca.append(paciente)
        elif 16 <= i < 24:
            pacientes_quarta.append(paciente)
        elif  24 <= i < 32:
            pacientes_quinta.append(paciente)
        elif 32 <= i < 40:
            pacientes_sexta.append(paciente)
    print("Segunda-feira:", pacientes_segunda, "\n")
    print("Terça-feira:", pacientes_terca, "\n")
    print("Quarta-feira:", pacientes_quarta, "\n")
    print("Quinta-feira:", pacientes_quinta, "\n")
    print("Sexta-feira:", pacientes_sexta, "\n")

print("resolver problema")

divisao_clientes_semana(pacientes_da_semana)



