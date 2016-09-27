print('Responda as perguntas apenas com SIM ou NAO')
perguntas = [input('1) Telefonou para a vitima? '),
             input('\n2) Esteve no local do crime? '),
             input('\n3) Mora Perto da Vitima? '),
             input('\n4) Devia para a vítima? '),
             input('\n5) Já trabalhou com a vítima? ')]
cont_sim = 0
cont_nao = 0

for respostas in perguntas:
    if respostas == 'sim':
        cont_sim = cont_sim + 1
    else:
        cont_nao = cont_nao + 1

if cont_sim == 5:
    print('\n###########################################'
          '\nConsideramos o entrevistado como : Assassino'
          '\n###########################################')
elif cont_sim > 2 and cont_sim <= 4:
    print('\n###########################################'
          '\nConsideramos o entrevistado como : Cumplice'
          '\n###########################################')
elif cont_sim == 2:
    print('\n###########################################'
          '\nConsideramos o entrevistado como : Suspeito'
          '\n###########################################')
else:
    print('\n###########################################'
          '\nConsideramos o entrevistado como : Inocente'
          '\n###########################################')