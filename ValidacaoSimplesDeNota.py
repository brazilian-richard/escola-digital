# autor: Richard da Silva - https://github.com/brazilian-richard/escola-digital/
# versão 0.1 (versão simplificada)

a = float(input("Qual é a 1a nota do aluno?"))
b = float(input("Qual é a 2a nota do aluno?"))
presenca = int(input("Qual é a presença do aluno? (0-100)"))

csum = (a + b) / 2

# print("A:", a, "B: ", b, "Soma de (A+B)/2: :", csum/2)

if ((presenca >= 75) or (presenca >= 70)):
    if((csum) == 10):
        print("Aluno aprovado com louvor.")
    elif (csum >= 7):
        print("Aluno aprovado.")
    elif (csum < 7):
        print("Aluno parcialmente aprovado. Recuperação.")
else:
    print("Aluno reprovado e sem direito a aulas de recuperação.")
