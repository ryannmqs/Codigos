#Lista de notas de estudantes:
print("Digite as notas dos estudantes (de 0 a 10). Digite -1 para encerrar a entrada de notas.")
notas = []
while True:
    nota = float(input("Digite as quatro notas do estudante: "))
    if nota == -1:
        break
    elif nota < 0 or nota > 10:
        print("Nota inválida, por favor digite uma nota de 0 a 10.")
    else:
        notas.append(nota)

def calcular_media(notas):
    total = sum(notas)
    media = total / len(notas)
    return media

#Arredondar a média
arredondar_media = lambda media: round(media, 1)

#Calcular a média das notas
media = calcular_media(notas)
media_arredondada = arredondar_media(media)

#Verificar aprovação
situacao = "Aprovado" if media_arredondada >= 7 else "Reprovado"

#resultados
print("Notas dos estudantes:", notas)
print("Média das notas:", media_arredondada)
print("Situação:", situacao)