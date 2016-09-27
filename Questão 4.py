print('Responda as perguntas apenas com SIM ou NAO')
perguntas = [input('1) Sabe ligar um computador ? '),
             input('\n2) Já trabalhou com o Windows 3.5 ? '),
             input('\n3) Já usou disquete? '),
             input('\n4) Sabe desligar o computador ? '),
             input('\n5) Sabe programar em python ? ')]
cont_sim = 0
cont_nao = 0

for respostas in perguntas:
    if respostas == 'sim':
        cont_sim = cont_sim + 1
    else:
        cont_nao = cont_nao + 1

if cont_sim == 5:
    print('\n###########################################'
          '\nConsideramos o entrevistado como : Hacker'
          '\n###########################################')
elif cont_sim == 3 and cont_sim == 4:
    print('\n###########################################'
          '\nConsideramos o entrevistado como : Sabe alguma coisa'
          '\n###########################################')
elif cont_sim == 2:
    print('\n###########################################'
          '\nConsideramos o entrevistado como : Tá aprendendo'
          '\n###########################################')
else:
    print('\n###########################################'
          '\nConsideramos o entrevistado como : Sabe de nada, inocente!!!'
          '\n###########################################')