# -*- coding: utf-8 -*-
"""Alana Souza - 202_Est_Repeticao_Manha.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1iP8ZPsmNaoNkPdz004JjU2cGi-gLzFgj

###1. Faça um algoritmo  que mostre 10 vezes a frase “Bem vindo a Fatec!”.
"""

contador = 1
while contador <= 10:
    print('Bem Vindo a Fatec!')
    contador = contador + 1

"""###2. Faça um algoritmo que mostre o cumprimento ‘Olá ‘ para o nome de alguém (4 pessoas). Exemplo ‘Olá Mariana’.
 
"""

contador = 1
while contador <=4:
  nome = (input('Digite seu nome: '))
  print('Olá',nome)
  contador = contador + 1

"""###3. Faça um algoritmo que mostre os valores de 0 a 15.

"""

contador = 0
while contador <16:
    print(contador)
    contador = contador + 1

"""###4. Faça um algoritmo que mostre os valores de 3 a 20.

"""

contador = 3
while contador <=20:
    print(contador)
    contador = contador + 1

"""###5. Faça um algoritmo que calcule e mostre a tabuada do 5.

"""

tabuada = 0
print('Tabuada de {}'.format(5))  
while (tabuada <= 10):  
  print('{0} X {1} = {2}'.format(tabuada, 5, (tabuada * 5)))  
  tabuada = tabuada + 1

"""###6. Faça um algoritmo que receba a idade de 10 pessoas, calcule e exiba a quantidade de pessoas maiores de idade, sendo que a maioridade é obtida após completar 18 anos.

"""

quantidadePessoas = 0
contador = 1
while contador <= 5:
    idade = int (input('Informe a idade: '))
    if idade >= 18:
        quantidadePessoas = quantidadePessoas + 1
    contador = contador + 1
print('Quantidade de pessoas maiores que 18 anos: ',quantidadePessoas)

"""###7. Escreva um algoritmo que receba 23 números, calcule e exiba a quantidade de números pares e impares.

"""

qtpar = 0
qtimpar = 0
contador = 1
while contador <= 23:
  numero = float (input('Informe um numero: '))
  if numero % 2 == 0:
    qtpar = qtpar + 1
    print('numero par')
  else:
    qtimpar = qtimpar + 1
    print('numero impar')
  contador = contador + 1
print('par',qtpar,'impar',qtimpar)

"""###8. Faça um algoritmo que calcule e exiba o salário reajustado de dez funcionários de acordo com a seguinte regra: 
Salário até 300, reajuste de 50%; 

Salários maiores que 300, reajuste de 30%.

"""

contador = 1
while contador <= 10:
  salario = float (input('Informe o salario:  '))
  if salario <=300:
    reajuste = salario + salario * 50/100
    print('Novo salario',reajuste)
  else:
    reajuste = salario + salario * 30/100
    print('Novo salario',reajuste)
  contador = contador + 1

"""###9. Faça um algoritmo que conheça 4 valores diferentes, some-os e mostre o resultado.

"""

contador = 1
somaNumeros = 0
while contador <= 4:
  numero = int (input('Informe um numero:  '))
  somaNumeros = somaNumeros + numero
  contador += 1
print('Total:',somaNumeros)

"""###10. Elabore um algoritmo que calcule e informe a média de idades de 5 alunos.

"""

soma = 0
for cont in range(1,6):
  numero = float(input("Digite sua nota: "))
  soma = soma + numero
media = soma / 5
print("A media final é de: ",media)

"""###11. Construir um algoritmo para calcular a média aritmética de preços de 5 produtos.

"""

soma = 0
for cont in range(1,6):
  numero = float(input("Digite o valor do produto R$ "))
  soma = soma + numero
media = soma / 4
print("A media final é de: ",media)

"""###12. Construir um algoritmo que, dado o valor de 20 preços de TV, determine e apresente o valor mais caro e mais barato entre eles.

"""

contador = 1
while contador <= 20:
  valor = float (input('Informe o valor da TV:  '))
  if contador == 1:
    caro = valor
    barato = valor
  elif valor >= caro:
    caro = valor
  elif valor <= barato:
    barato = valor
  contador = contador + 1
print('TV mais cara:',caro,'R$')
print('TV mais barata',barato,'R$')

"""###13. Faça um algoritmo que leia de dez alunos altura e nome.  Mostre o aluno mais alto e mais baixo e seus respectivos nomes.

"""

contador = 1
while contador <= 10:
  nome = input('Informe seu nome: ')
  altura = float (input('Informe sua altura:  '))
  if contador == 1:
    alto = altura
    nomeAlto = nome
    baixo = altura
    nomeBaixo = nome
  elif altura >= alto:
    alto = altura
    nomeAlto = nome
  elif altura <= baixo:
    baixo = altura
    nomeBaixo = nome
  contador = contador + 1
print('aluno',nomeAlto,'é mais alto com',alto,'metros')
print('aluno',nomeBaixo,'é mais baixo com',baixo,'metros')

"""### 14. Um funcionário de uma empresa recebe, anualmente, aumento salarial.

**Sabe-se que:**

* Esse funcionário foi contratado em 2005, com salário inicial de R$ 1.000,00.
* Em 2006, ele recebeu aumento de 1,5% sobre seu salário inicial.
* A partir de 2007, os aumentos salariais sempre corresponderam ao dobro do percentual do ano anterior.

**Faça um programa que determine o salário atual desse funcionário.**

```
LEIA ano_atual

salario_inicial =1000
percentual_de_aumento_do_ano  = 1.5 / 100

aumento_do_ano = salario_inicial * percentual_de_aumento_do_ano
salario_do_ano = salario_inicial + aumento_do_ano

PARA ano NO INTERVALO DE 2007 ATÉ ano_atual + 1
    percentual_do_ano = percentual_do_ano * 2
    aumento_do_ano = salario_do_ano * percentual_do_ano
    salario_do_ano = salario_do_ano + aumento_do_ano
    
ESCREVA ano, salario_do_ano
```

"""

ano_atual = int (input('Informe o ano atual: '))
salario_inicial = 1000
percentual_de_aumento_do_ano  = 1.5 / 100
aumento_do_ano = salario_inicial * percentual_de_aumento_do_ano
salario_do_ano = salario_inicial + aumento_do_ano
print('Ano 2006 - Salário novo: ',salario_do_ano)
for ano in range(2007,ano_atual + 1):
    percentual_de_aumento_do_ano = percentual_de_aumento_do_ano * 2
    aumento_do_ano = salario_do_ano * percentual_de_aumento_do_ano
    salario_do_ano = salario_do_ano + aumento_do_ano
    print(f'Ano {ano} - salário novo R$ {salario_do_ano:.2f}')

"""### 15. Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. Foram obtidos os seguintes dados:

* nome da cidade;
* número de veículos de passeio;
* número de acidentes de trânsito com vítimas.

**Deseja-se saber:**

* o maior  índice de acidentes de trânsito e a que cidades pertence;
* o menor índice de acidentes de trânsito e a que cidades pertence;
* qual é a média de veículos nas cinco cidades juntas;
* qual é a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.

#### ALGORITMO
---

```
total_cidades = 5
somatoria_veiculos_cidades = 0
somatoria_acidentes_cidades_2000_veiculos = 0
numero_cidades_2000_veiculos = 0

PARA cidade NO INTERVALO total_cidades
    LEIA nome_cidade, numero_veiculos, numero_acidentes
    SE cidade == 0
        maior_casos_acidentes = numero_acidentes
        cidade_maior_casos_acidentes = nome_cidade
        menor_casos_acidentes = numero_acidentes
        cidade_menor_casos_acidentes = nome_cidade
    SENÃO
        SE numero_acidentes > maior_casos_acidentes
             maior_casos_acidentes = numero_acidentes
             cidade_maior_casos_acidentes = nome_cidade
        SE numero_de_acidentes < menor_casos_acidentes
            menor_caso_acidentes = numero_acidentes
            cidade_menor_casos_acidentes = nome_cidade
                
    somatoria_veiculos_cidades += numero_veiculos
    #ou somatoria_veiculos_cidades = somatoria_veiculos_cidades + numero_veiculos
    
    SE numero_veiculos > 2000
        soma_acidentes_cidades_2000_veiculos += numero_acidentes
        numero_cidades_2000_veiculos += 1
        
media_carros_cidades = somatoria_veiculos_cidades / total_cidades

SE numero_cidades_2000_veiculos == 0
    ESCREVA “Não foi informada nenhuma cidade com menos de 2000 veículos”
SENAO
    media_acidentes_cidade_2000_veiculos = soma_acidentes_cidades_veiculos / numero_cidades_2000_veiculos
    
ESCREVA cidade_maior_casos_acidentes,maior_casos_acidentes
ESCREVA cidade_menor_casos_acidentes,menor_casos_acidentes
ESCREVA media_carros_cidades
ESCREVA media_acidentes_cidade_2000_veiculos
```

"""

total_cidades = 5
somatoria_veiculos_cidades = 0
somatoria_acidentes_cidades_2000_veiculos = 0
numero_cidades_2000_veiculos = 0
for cidade in range(total_cidades):
  nome_cidade = (input('Digite o nome da cidade '))
  numero_veiculos = int (input('Digite o numero de veiculos '))
  numero_acidentes = int (input('Digite o numero de acidentes '))
  if cidade == 0:
        maior_casos_acidentes = numero_acidentes
        cidade_maior_casos_acidentes = nome_cidade
        menor_casos_acidentes = numero_acidentes
        cidade_menor_casos_acidentes = nome_cidade
  else:
      if numero_acidentes > maior_casos_acidentes:
             maior_casos_acidentes = numero_acidentes
             cidade_maior_casos_acidentes = nome_cidade
      if numero_acidentes < menor_casos_acidentes:
             menor_caso_acidentes = numero_acidentes
             cidade_menor_casos_acidentes = nome_cidade
             somatoria_veiculos_cidades = somatoria_veiculos_cidades + numero_veiculos
  if numero_veiculos > 2000:
        somatoria_acidentes_cidades_2000_veiculos += numero_acidentes
        numero_cidades_2000_veiculos += 1
  media_carros_cidades = somatoria_veiculos_cidades / total_cidades
if numero_cidades_2000_veiculos == 0:
    print('Não foi informada nenhuma cidade com menos de 2000 veículos')
else:
    media_acidentes_cidade_2000_veiculos = soma_acidentes_cidades_veiculos / numero_cidades_2000_veiculos
    print('A media de acidentes nas 5 cidades é de',media_acidentes_cidade_2000_veiculos)
print('A cidade com maior casos é',cidade_maior_casos_acidentes,maior_casos_acidentes)
print('A cidade com menor casos é',cidade_menor_casos_acidentes,menor_casos_acidentes)
print('A media de carros nas 5 cidades é de',media_carros_cidades)

"""### 16. Faça um programa que monte os oito primeiros termos da sequência de Fibonacci.

#### ALGORITMO
___
```
numero_de_elementos_da_sequencia = 8
elementoN = 0
elementoNmais1 = 1

ESCREVA elementoN
ESCREVA elementoNmais1

PARA elemento NO INTERVALO DE 3 ATÉ numero_de_elementos_da_sequencia
    valor_do_fibonacci_atual = elementoN + elementoNmais1
   
    ESCREVA valor_do_fibonacci_atual
    
    elementoN = elementoNmais1
    elementoNmais1 = valor_do_fibonacci_atual
    
```
"""

numero_de_elementos_da_sequencia = 8
elementoN = 0
elementoNmais1 = 1
print(elementoN)
print(elementoNmais1)
for elemento in range( 3, numero_de_elementos_da_sequencia):
    valor_do_fibonacci_atual = elementoN + elementoNmais1
    print(valor_do_fibonacci_atual)
    elementoN = elementoNmais1
    elementoNmais1 = valor_do_fibonacci_atual

"""### 17. Faça um programa que leia o número de termos, determine e mostre os valores de acordo com a série a seguir:

Série = 2, 7, 3, 4, 21, 12, 8, 63, 48, 16, 189, 192, 32, 567, 768...

####ALGORITMO
---
```
LEIA numero_de_termos

termo1 = 2
termo2 = 7
termo3 = 3

termo_atual = 4

ENQUANTO termo_atual <= numero_de_termos
    ESCREVA termo1, termo2, termo3
    
    termo1 = termo1 * 2
    ESCREVA termo1
    termo_atual += 1
    
    SE termo_atual <= numero_de_termos
        termo2 = termo2 * 3
        ESCREVA termo2
        termo_atual += 1
        
    SE termo_atual <= num_termos
        termo3 = termo3 * 4
        ESCREVA termo3
        termo_atual += 1
```
"""

numero_de_termos = int (input('Determine um numero de contagem para os termos '))
termo1 = 2
termo2 = 7
termo3 = 3
print(termo1, termo2, termo3)
termo_atual = 4
while termo_atual <= numero_de_termos:  
    termo1 = termo1 * 2
    print(termo1)
    termo_atual += 1    
    if termo_atual <= numero_de_termos:
        termo2 = termo2 * 3
        print(termo2)
        termo_atual += 1
        if termo_atual <= numero_de_termos:
            termo3 = termo3 * 4
            print(termo3)
            termo_atual += 1

"""### 18. Faça um programa que receba duas notas de seis alunos. Calcule e mostre:

* a média aritmética das duas notas de cada aluno; e
* a mensagem que está na tabela a seguir:


Média aritimética | Mesagem
---|---
Até 3|Reprovado
Entre 3 e 7 |Exame
De 7 para cima| Aprovado

* o total de alunos aprovados;
* o total de alunos de exame;
* o total de alunos reprovados;
* a média da classe.
"""

aprovados = 0
exame = 0
reprovados = 0
mediaClasse = 0
contador = 0
print(''' 
  Média Aritmetica 
  Até 3 = Reprovado
  Entre 3 e 7 = Exame 
  De 7 para cima = Aprovado''')
while contador <6:
  nome = input('Insira seu nome:  ')
  nota1 = float (input('Insira a primeira nota: '))
  nota2 = float (input('Insira a segunda nota:  '))
  media = (nota1 + nota2) / 2
  print(nome,'sua média é de',media,'pontos.')
  contador = contador + 1
  if media <3:
    reprovados = reprovados + 1
    print('Reprovado.')
  elif media <7:
    print('Exame.')
    exame = exame + 1
  else:
    aprovados = aprovados + 1
    print('Aprovado.')
mediaClasse = media / 6
print('Numero de aprovados:',aprovados)
print('Numero de quem ficou para exame:',exame)
print('Numero de reprovados:',reprovados)
print('Media da sala foi de',mediaClasse)

"""### 19. Em uma fábrica trabalham homens e mulheres divididos em três classes:

* trabalhadores que fazem até 30 peças por mês — classe 1;
* trabalhadores que fazem de 31 a 50 peças por mês — classe 2;
* trabalhadores que fazem mais de 50 peças por mês — classe 3.

** Os salários são compostos da sequinte maneira:**

* A classe 1 recebe salário mínimo.
* A classe 2 recebe salário mínimo mais 3% deste salário por peça, acima das 30 peças iniciais.
* A classe 3 recebe salário mínimo mais 5% desse salário por peça, acima das 30 peças iniciais.

** Faça um programa que receba:**

* o número do operário,
* o número de peças fabricadas no mês,
* o sexo do operário,

**Calcule e mostre:**

* o número do operário e seu salário;
* o total da folha de pagamento da fábrica;
* o número total de peças fabricadas no mês;
* a média de peças fabricadas pelos homens;
* a média de peças fabricadas pelas mulheres; e
* o número do operário ou operária de maior salário.

**A fábrica possui 15 operários.**

#### ALGORITMO
---
```
total_de_operarios = 15
valor_do_salario_minimo = 954

total_da_folha_de_pagamento_no_mes = 0
total_de_pecas_fabricadas_no_mes = 0

media_das_pecas_fabricados_por_homens = 0
media_das_pecas_fabricados_por_mulheres = 0

total_de_homens = 0
total_de_mulheres = 0

meta_minima = 30
meta_classe3 = 50

porcentagem_de_bonus_da_classe1 = 0
porcentagem_de_bonus_da_classe2 = 2 / 100
porcentagem_de_bonus_da_classe3 = 3 / 100

total_de_operarios_homens = 0
total_de_operarios_mulheres = 0

somatorio_das_pecas_fabricadas_por_homens = 0
somatorio_das_pecas_fabricadas_por_mulheres = 0

maior_salario_entre_os_operarios = -1

PARA operario NO INTERVALO de total_de_operarios
    ESCREVA “Digite o número do operário “
    LEIA numero_do_operario
    
    ESCREVA “Digite o sexo do operário (M ou F) “
    LEIA sexo_do_operario
    
    ESCREVA “Digite o total de peças fabricadas pelo operario“
    LEIA total_de_pecas_fabricadas_pelo_operario
    
    SE total_de_pecas_fabricadas_pelo_operario <= meta_minima
        porcentagem_da_classe_do_operario = porcentagem_de_bonus_da_classe1
    SENAO SE total_de_pecas_do_operario >= meta_classe3
        porcentagem_da_classe_do_operario = porcentagem_de_bonus_da_classe3
    SENAO
          porcentagem_da_classe_do_operario = porcentagem_de_bonus_da_classe2
          
    SE ttotal_de_pecas_fabricadas_pelo_operario > meta_minima
        producao_acima_da_meta = total_de_pecas_fabricadas_pelo_operario - meta_minima
    SENAO
        producao_acima_da_meta = 0
    
    bonus_de_producao = valor_do_salario_minimo * porcentagem_da_classe_do_operario * producao_acima_da_meta
    
    salario_do_operario = valor_do_salario_minimo + bonus_de_producao
    
    ESCREVA numero_do_operario, salario_do_operario
    
    total_da_folha_de_pagamento_no_mes += salario_do_operario 
    total_de_pecas_fabricadas_no_mes += total_de_pecas_fabricadas_pelo_operario
    
    SE sexo_do_operario ESTA EM "Hh"
        total_de_homens += 1
        somatorio_das_pecas_fabricadas_por_homens += total_de_pecas_fabricadas_pelo_operario
        
    SE sexo_do_operario ESTA EM "Mm"
        total_de_mulheres += 1
        somatorio_das_pecas_fabricadas_por_mulheres += total_de_pecas_fabricadas_pelo_operario
        
    SE salario_do_operario > maior_salario_entre_os_operarios
        numero_do_operario_com_o_maior_salario = numero_do_operario
        maior_salario_entre_os_operarios = salario_do_operario
        
media_de_pecas_fabricadas_por_homens = somatorio_das_pecas_fabricadas_por_homens / total_de_homens

media_de_pecas_fabricada_por_mulheres = somatorio_das_pecas_fabricadas_por_mulheres / total_de_mulheres

IMPRIMA total_da_folha_de_pagamento_no_mes
IMPRIMA total_de_pecas_fabricadas_no_mes
IMPRIMA media_de_pecas_fabricada_por_homens
IMPRIMA media_de_pecas_fabricada_por_mulheres
IMPRIMA numero_do_operario_com_o_maior_salario
```
"""

total_de_operarios = 15
valor_do_salario_minimo = 954
total_da_folha_de_pagamento_no_mes = 0
total_de_pecas_fabricadas_no_mes = 0
media_de_pecas_fabricadas_por_homens = 0
media_das_pecas_fabricados_por_mulheres = 0
total_de_homens = 0
total_de_mulheres = 0
meta_minima = 30
meta_classe3 = 50
porcentagem_de_bonus_da_classe1 = 0
porcentagem_de_bonus_da_classe2 = 2 / 100
porcentagem_de_bonus_da_classe3 = 3 / 100
total_de_operarios_homens = 0
total_de_operarios_mulheres = 0
somatorio_das_pecas_fabricadas_por_homens = 0
somatorio_das_pecas_fabricadas_por_mulheres = 0
maior_salario_entre_os_operarios = -1
for operario in range(total_de_operarios):
    numero_do_operario = int (input('Digite o número do operário: '))
    sexo_do_operario = input('Digite o sexo do operário em maiúsculo (M ou H): ')
    total_de_pecas_fabricadas_pelo_operario = int (input('Digite o total de peças fabricadas pelo operario: '))
    if total_de_pecas_fabricadas_pelo_operario <= meta_minima:
        porcentagem_da_classe_do_operario = porcentagem_de_bonus_da_classe1
    elif total_de_pecas_do_operario >= meta_classe3:
        porcentagem_da_classe_do_operario = porcentagem_de_bonus_da_classe3
    else:
          porcentagem_da_classe_do_operario = porcentagem_de_bonus_da_classe2
    if total_de_pecas_fabricadas_pelo_operario > meta_minima:
        producao_acima_da_meta = total_de_pecas_fabricadas_pelo_operario - meta_minima
    else:
        producao_acima_da_meta = 0
    bonus_de_producao = valor_do_salario_minimo * porcentagem_da_classe_do_operario * producao_acima_da_meta
    salario_do_operario = valor_do_salario_minimo + bonus_de_producao
    print('Numero do operário:',numero_do_operario,'Salario do operario:',salario_do_operario)
    total_da_folha_de_pagamento_no_mes += salario_do_operario 
    total_de_pecas_fabricadas_no_mes += total_de_pecas_fabricadas_pelo_operario
    if sexo_do_operario == 'H':
        total_de_homens += 1
        somatorio_das_pecas_fabricadas_por_homens += total_de_pecas_fabricadas_pelo_operario
    if sexo_do_operario == 'M':
        total_de_mulheres += 1
        somatorio_das_pecas_fabricadas_por_mulheres += total_de_pecas_fabricadas_pelo_operario
    if salario_do_operario > maior_salario_entre_os_operarios:
        numero_do_operario_com_o_maior_salario = numero_do_operario
        maior_salario_entre_os_operarios = salario_do_operario
media_de_pecas_fabricadas_por_homens = somatorio_das_pecas_fabricadas_por_homens / total_de_homens
media_de_pecas_fabricadas_por_mulheres = somatorio_das_pecas_fabricadas_por_mulheres / total_de_mulheres
print('Total da folha de pagamento:',total_da_folha_de_pagamento_no_mes,'R$')
print('Total de peças fabricadas no mês:',total_de_pecas_fabricadas_no_mes,'peças.')
print('Média de peças fabricadas por Homens:',media_de_pecas_fabricadas_por_homens,'peças.')
print('Média de peças fabricadas por mulheres:',media_de_pecas_fabricadas_por_mulheres,'peças.')
print('Numero do operário com o maior salario:',numero_do_operario_com_o_maior_salario)

"""###  20. Foi feita uma pesquisa com as crianças de uma determinada localidade. Faça um programa que:

* leia o número de crianças nascidas no período;
* identifique o sexo (M ou F) e a idade da criança.

**O programa deve calcular e mostrar:**

* a percentagem de crianças do sexo marculino;
* a percentagem de crianças do sexo feminino;
* a percentagem de crianças menores que 24 meses.

**Observação:

porcentagem_de_meninos = total_de_meninos / total_de_criancas_nascidas * 100

porcentagem_de_meninas = total_de_meninas / total_de_criancas_nascidas * 100
porcentagem_de_criancas_menores_de_24_mese=criancas_menores_de_24_mese/total_de_criancas_nascidas*100
"""

totalMeninas = 0
totalMeninos = 0
menores24Meses = 0
totalRep = int (input('Digite o numero de crianças '))
for criancas in range(totalRep):
  sexo = input('Digite o sexo da criança (M/F):  ')
  idade = int (input('Digite a idade da criança:  '))
  if sexo == 'M':
    totalMeninos += 1
  else:
    totalMeninas += 1
  if idade <=2:
    print('Criança menor que 24 meses')
    menores24Meses += 1
porcentagemMeninos = totalMeninos / totalRep * 100
porcentagemMeninas = totalMeninas / totalRep * 100 
porcentagemmenores24Meses = menores24Meses / totalRep * 100
print('A porcentagem de crianças do sexo masculino é de',porcentagemMeninos)
print('A porcentagem de crianças do sexo feminino é de',porcentagemMeninas)
print('A porcentagem de crianças menores que 24 meses é de',porcentagemmenores24Meses)

"""### 21.  Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes dados:

* valor da dívida,
* valor dos juros, 
* quantidade de parcelas
* valor da parcela.

**Os juros e a quantidade de parcelas seguem a tabela:** 

Quantidade de parcelas |  % de juros sobre o valor inicial da dívida
---|---
1 |0
3 |10
6 |15
9 |20
12 |25

**Exemplo de saída do programa:**

Valor da dívida|Valor dos juros (em reais) | Quantidade de parcelas| Valor da parcela
---|---|---|---
1.000,00 |0| 1| 1.000,00
1.100,00 |100 |3| 366,67
1.150,00 |150 |6| 191,67
"""

totalDividas = int (input('Digite o numero de dividas '))
for dividas in range(totalDividas):
  divida = float (input('Digite o valor da divida:  '))
  parcela = int (input('Digite a quantidade de parcelas:  '))
  if parcela == 1:
    total1 = 0
    totalParcela = divida
    print('\n Valor da dívida =',divida, '\n Valor dos juros (em reais) =',total1, '\n Quantidade de parcelas = 1', '\n Valor da parcela =',totalParcela)
  if parcela == 3:
    total3 = (divida*10)/100
    totalParcela = (divida + total3) / 3
    print('\n Valor da dívida =',divida, '\n Valor dos juros (em reais) =',total3, '\n Quantidade de parcelas = 3', '\n Valor da parcela =',totalParcela)
  if parcela == 6:
    total6 = (divida*15)/100
    totalParcela = (divida + total6) / 6
    print('\n Valor da dívida =',divida, '\n Valor dos juros (em reais) =',total6, '\n Quantidade de parcelas = 6', '\n Valor da parcela =',totalParcela)
  if parcela == 9:
    total9 = (divida*20)/100
    totalParcela = (divida + total9) / 9
    print('\n Valor da dívida =',divida, '\n Valor dos juros (em reais) =',total9, '\n Quantidade de parcelas = 9', '\n Valor da parcela =',totalParcela)
  if parcela == 12:
    total12 = (divida*25)/100
    totalParcela = (divida + total12) / 12
    print('\n Valor da dívida =',divida, '\n Valor dos juros (em reais) =',total12, '\n Quantidade de parcelas = 12', '\n Valor da parcela =',totalParcela)

"""### 22. Faça um programa que receba:

* o preço unitário,
* a refrigeração (S para os produtos que necessitem de refrigeração e N para os que não necessitem)
* a categoria (A — alimentação; L — limpeza; e V — vestuário)

**Calcule e mostre:**

* O custo de estocagem, calculado de acordo com a tabela a seguir.


Preço unitário| Refrigeração| Categoria| Custo de estocagem
---|---|---|---
Até 20 | - |  A| 2,00
Até 20|-  |L  |3,00
Até 20| - |  V|4,00
----------------------|----------------------|----------------------|----------------------
Entre 20 e 50 (inclusive)|S  | - |6,00
Entre 20 e 50 (inclusive)|  N|  -| 0,00 |
----------------------|----------------------|----------------------|----------------------
Maior que 50| S| A |  5,00|
Maior que 50| S | L |  2,00| 
Maior que 50| S| V |  4,00| 
Maior que 50|  N|A ou V  |0,00  | 
Maior que 50|  N| L | 1,00 | 


* O imposto calculado de acordo com as regras a seguir:
  * Se o produto possuir **categoria A** e **refrigeração S**, seu imposto será de 2% sobre o preço
unitário; caso contrário, será de 4%.
  * O preço final, ou seja, preço unitário mais custo de estocagem mais imposto.
  * A classificação calculada usando a tabela a seguir.

Preço final| Classificação
---|---
Até 20,00 |Barato
Entre 20,00 e  100,00 (inclusive)|Normal
Acima de R$ 100,00| Caro

* A média dos valores adicionais, ou seja, a média dos custos de estocagem e dos impostos dos doze produtos.
* O maior preço final.
* O menor preço final.
* O total dos impostos.
* A quantidade de produtos com classificação barato.
* A quantidade de produtos com classificação caro.
* A quantidade de produtos com classificação normal.

####ALGORITMO
---

```
total_de_produtos = 12

total_de_produtos_baratos = 0
total_de_produtos_normais = 0
total_de_produtos_caros = 0

total_de_custos_adicionais = 0

PARA produto NO INTERVALO DE total_de_produtos
    LEIA preco_do_produto, produto_necessita_de_refrigeracao, categoria_do_produto
    
    SE preco_do_produto <= 20
        SE categoria_do_produto == "A"
            custo_de_estocagem = 2
        SE categoria_do_produto == "L"
            custo_de_estocagem = 3
        SE categoria_do_produto == "V"
            custo_de_estocagem = 4
           
    SE  prodo_do_produto > 20 E preco_do_produto <= 50
        SE produdo_necessida_de_refrigeracao == "S"
            custo_de_estocagem = 6
        SENAO
            custo_de_estocagem = 0
            
    SE preco_do_produto > 50
        SE produdo_necessida_de_refrigeracao == "S"
            SE categoria_do_produto == "A"
                custo_de_estocagem = 5
            SE categoria_do_produto == "L"
                custo_de_estocagem = 2
            SE categoria_do_produto == "V"
                custo_de_estocagem = 4
        SENAO
            SE categoria_do_produto = "A" OU categoria_do_produto = "V"
                custo_de_estocagem = 0
            SE cagegoria_do_produto = "L"
                custo_de_estocagem = 1
        
    SE categoria_sobre_o_produto == "A" e produdo_necessida_de_refrigeracao == "S"
        imposto_do_produto = 2 / 100
    SENAO
        imposto_sobre_o_produto = 4 / 100
    
    preco_final_sobre_produto = preco_do_produto + custo_de_estocagem_do_produto + imposto_sobre_o_produto
  
  ESCREVA custo_de_estocagem_do_produto, imposto_sobre_o_produto, preco_final_do_produto
  
  SE preco_final_sobre_produto <= 20
      total_de_produtos_baratos += 1
      classificacao_do_produto = "PRODUTO BARATO"
      
  SE preco_final_sobre_produto >  20 E preco_final_sobre_produto <=  20
      total_de_produtos_normais += 1
      classificacao_do_produto = "PRODUTO NORMAL"
      
  SE preco_final_sobre_produto >  100
      total_de_produtos_caros += 1
      classificacao_do_produto = "PRODUTO CARO"
      
  custo_adicional_do_produto = custo_de_estocagem_do_produto + imposto_sobre_o_produto
   
   total_de_custo_adicionais_de_todos_produtos += custo_adicional_do_produto
   total_de_impostos_de_todos_os_produtos += imposto_sobre_o_produto
   
   SE produto == 0
      preco_do_produto_mais_caro = preco_final_do_produto
      preco_do_produto_mais_barato = preco_final_do_produto
   SENAO
      SE preco_do_produto_mais_caro < preco_final_do_produto
          preco_do_produto_mais_caro = preco_final_do_produto
      SE preco_do_produto_mais_barato > preco_final_do_produto
          preco_do_produto_mais_barato = preco_final_do_produto
          
media_dos_valores_adicionais = total_de_custo_adicionaisl_de_todos_produtos / total_de_produtos

ESCREVA media_dos_valores_adicionais
ESCREVA preco_do_produto_mais_caro
ESCREVA preco_do_produto_mais_barato
ESCREVA total_de_produtos_baratos
ESCREVA total_de_produtos_normais
ESCREVA total_de_produtos_caros
   
```
"""

total_de_produtos = 12 
total_de_produtos_baratos = 0
total_de_produtos_normais = 0
total_de_produtos_caros = 0
custo_de_estocagem = 0
total_de_custos_adicionais = 0
total_de_impostos_de_todos_os_produtos = 0
preco_do_produto_mais_caro  = 0
preco_final_do_produto = 0
preco_do_produto_mais_barato = 0

for produto in range(0,12):
    preco_do_produto = float (input('Insira o preço do produto: '))
    produto_necessita_de_refrigeracao = (input('Produto necessita de refrigeracao? (s/n) '))
    categoria_do_produto=(input('Digite a categoria do produto:  '))
    if preco_do_produto <= 20:
	    if categoria_do_produto == 'a':
		    custo_de_estocagem = 2
    if categoria_do_produto == '1':
        custo_de_estocagem = 3
        if categoria_do_produto == 'v':
            custo_de_estocagem = 4
    if preco_do_produto > 20 and preco_do_produto <= 50:
        if produto_necessita_de_refrigeracao == 's':
            custo_de_estocagem = 6
        else:
            custo_de_estocagem = 0
 
    if preco_do_produto > 50:
        if produto_necessita_de_refrigeracao == 's':
            if categoria_do_produto == 'a':
                custo_de_estocagem = 5
            if categoria_do_produto == 'l':
                custo_de_estocagem = 2
            if categoria_do_produto == 'v':
                custo_de_estocagem = 4
        else:
            if categoria_do_produto == 'a' or categoria_do_produto == 'v':
                custo_de_estocagem = 0
            if categoria_do_produto == 'L':
                custo_de_estocagem = 1
 
    if categoria_do_produto == 'a' and produto_necessita_de_refrigeracao == 's':
        imposto_do_produto = preco_do_produto * 2 / 100
    else:
        imposto_do_produto = preco_do_produto * 4 / 100

    preco_final_produto = preco_do_produto + custo_de_estocagem + imposto_do_produto
    print('Custo de estocagem',custo_de_estocagem)
    print('Imposto sobre o produto',imposto_do_produto)
    print('Preco final produto',preco_final_produto)
 
    if preco_final_produto <= 100:
      total_de_produtos_baratos += 1
      classificacao_do_produto = 'PRODUTO BARATO'
 
    if preco_final_produto >100 and preco_final_produto < 1000:
      total_de_produtos_normais += 1
      classificacao_do_produto = 'PRODUTO NORMAL'
 
    if preco_final_produto >= 1000:
      total_de_produtos_caros += 1
      classificacao_do_produto = 'PRODUTO CARO'
 
    custo_adicional_do_produto = custo_de_estocagem + imposto_do_produto
 
    total_de_custos_adicionais += custo_adicional_do_produto
    total_de_impostos_de_todos_os_produtos += imposto_do_produto
 
    if produto == 0:
        preco_do_produto_mais_caro = preco_final_produto
        preco_do_produto_mais_barato = preco_final_produto
    else:
        if preco_final_produto > preco_do_produto_mais_caro:
            preco_do_produto_mais_caro = preco_final_produto
        if preco_final_produto < preco_do_produto_mais_barato:
            preco_do_produto_mais_barato = preco_final_produto
 
media_dos_valores_adicionais = total_de_custos_adicionais / total_de_produtos
 
print('Média dos valores adicionais',media_dos_valores_adicionais)
print('Preco do produto mais caro',preco_do_produto_mais_caro)
print('Preco do produto mais barato',preco_do_produto_mais_barato)
print('Total de produtos baratos',total_de_produtos_baratos)
print('Total de produtos normais',total_de_produtos_normais)
print('Total de produtos caros',total_de_produtos_caros)

"""### 23.Faça um programa que:

* leia um valor N inteiro e positivo
* Calcule e mostre o valor de E, conforme a fórmula:

E = $1 +\frac{1}{1!}+\frac{1}{2!}+\frac{1}{3!}+\frac{1}{4!}+ . . . +\frac{1}{N!}$

**Dica:** Não use função pronta da linguagem Python
"""

numero = int(input("Fatorial de: ") )
resultado=1
for n in range(1,numero+1):
    resultado *= n
print(resultado)

"""###24.Faça um programa para calcular a tabuada do 2 até a do 9. USE DUAS ESTRUTURAS DE REPETIÇÃO"""

for i in range(2,10):
 for j in range(1,11):
  print(i,'x',j,'=',i*j)

"""###25. Elabore um algoritmo que informada a idade de 10 nadadores o mesmo terá condições de classificar em uma das seguintes categorias: infantil = 5 - 10 anos; juvenil = 11-17 anos; adulto >= maiores de 18 anos.


"""

nadadores = 10
idade = int (idade)
for nadadores in range(nadadores):
  idade = int(input('Digite a sua idade: '))
  if idade >= 5 and idade <=10:
    print('Você é um nadador da categoria Infantil')
  if idade >=11 and idade <=17:
    print('Você é um nadador da categoria Juvenil')
  if idade >=18:
    print('Você é um nadador da categoria Adulto')[]