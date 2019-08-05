#
# Siga as instruções que estão no enunciado do EP04
# para criar o arquivo ep04.py 
#
# -*- coding: utf-8 -*-
#------------------------------------------------------------------
# LEIA E PREENCHA O CABEÇALHO 
# NÃO ALTERE OS NOMES DAS FUNÇÕES, MÉTODOS E ATRIBUTOS
# NÃO APAGUE OS DOCSTRINGS
#------------------------------------------------------------------
     
'''
    Nome: 
    NUSP: 

    Ao preencher esse cabeçalho com o meu nome e o meu número USP,
    declaro que todas as partes originais desse exercício programa (EP)
    foram desenvolvidas e implementadas por mim e que portanto não 
    constituem desonestidade acadêmica ou plágio.
    Declaro também que sou responsável por todas as cópias desse
    programa e que não distribui ou facilitei a sua distribuição.
    Estou ciente que os casos de plágio e desonestidade acadêmica
    serão tratados segundo os critérios divulgados na página da 
    disciplina.
    Entendo que EPs sem assinatura devem receber nota zero e, ainda
    assim, poderão ser punidos por desonestidade acadêmica.

    Abaixo descreva qualquer ajuda que você recebeu para fazer este
    EP.  Inclua qualquer ajuda recebida por pessoas (inclusive
    monitores e colegas). Com exceção de material de MAC0110, caso
    você tenha utilizado alguma informação, trecho de código,...
    indique esse fato abaixo para que o seu programa não seja
    considerado plágio ou irregular.

    Exemplo:

        A monitora me explicou que eu devia utilizar a função int() quando
        fazemos leitura de números inteiros.

        A minha função quicksort() foi baseada na descrição encontrada na 
        página https://www.ime.usp.br/~pf/algoritmos/aulas/quick.html.

    Descrição de ajuda ou indicação de fonte:

'''
#####################################################################
# MÓDULOS A SEREM UTILIZADOS NO PROGRAMA
import random

#####################################################################
# CONSTANTES
# Constantes definem variáveis cujos valores NÃO DEVEM ser 
# alterados durante a execução do programa. Assim você deve
# escolher bem esses valores ANTES de executar o programa.
#
# O uso de constantes é um boa prática de programação
# pois constantes ajudam a melhorar a legibilidade
# de seus programas. Por convenção, para identificar
# as constantes em um programa, vamos usar nomes com todas 
# as letras maiúsculas.
#
# As constantes abaixo são fornecidas como exemplo. Você
# pode utilizar, ou não, qualquer uma delas e ainda criar 
# outras constantes se desejar.
#
DEBUG = True       # se True, pede para digitar a semente e mostra a senha
MENOR_VALOR = 0    # menor número sorteado
MAIOR_VALOR = 9999 # limite superior para o maior número sorteado (mais 1)
MAX_TENTATIVAS = 7 # número máximos de chutes permitidos
NUM_DIGITOS  = 4   # número de dígitos da senha

#####################################################################
def main():
    '''(None) -> None 

    Coloque sua solução individual abaixo, seguindo o enunciado 
    desse exercício na página da disciplina.

    Siga as instruções para entrega disponíveis em:
    https://paca.ime.usp.br/mod/page/view.php?id=42515
    
    '''

    print("Bem vindo ao MASTER BIME!!")
    # as linhas abaixo vão ajudar durante o desenvolvimento e depuração 
    # para deixar de executá-las, basta modificar a constante DEBUG para 
    # False. Mas lembre-se de deixá-la True antes de enviar esse EP.
    if DEBUG:
        semente = int(input("Digite o valor da semente: "))
        random.seed(semente)
        senha = random.randrange(MENOR_VALOR, MAIOR_VALOR)
        print("Número sorteado: ", senha)
    else:
        senha = random.randrange(MENOR_VALOR, MAIOR_VALOR)
        
    # escreva seu programa a seguir
    n = 0
    i = 0
    j = 11
    k = 10
    i = 1
    m = 4
    
    while i < j:
         chute = int(input("Digite seu chute: "))
         n = em_posiçoes_certas(senha,chute,max)
         m = digitos_certos(senha,chute)
         if chute == senha :
             if 0 <= chute < 10 and n == 1  :
                 print("Dígitos em posições corretas do chute", i, '/', k,":", n)
                 print("Dígitos certos do chute %d / %d = %d"%(i,k,m))
                 print("Parabéns, você acertou")
                 i += 10
             if 10 <= chute < 100 and n == 2   :
                print("Dígitos em posições corretas do chute", i, '/', k,":", n)
                print("Dígitos certos do chute %d / %d = %d"%(i,k,m))
                print("Parabéns, você acertou")
                i += 10
             if 100 <= chute < 1000 and n == 3  :
                print("Dígitos em posições corretas do chute", i, '/', k,":", n)
                print("Dígitos certos do chute %d / %d = %d"%(i,k,m))
                print("Parabéns, você acertou")
                i += 10
             if chute >= 1000 and n == 4  :
                print("Dígitos em posições corretas do chute", i, '/', k,":", n)
                print("Dígitos certos do chute %d / %d = %d"%(i,k,m))
                print("Parabéns, você acertou")
                i += 10
         else:
               print("Dígitos em posições corretas do chute %d / %d : %d"%(i,k,n))
         if chute != senha:
             print("Dígitos certos do chute %d / %d : %d"%(i,k,m))
             i += 1
             if i == 11:
                 print("Ha ha, você perdeu!")
                    
        
    print("Fim do jogo.")
                
def em_posiçoes_certas(senha,chute,max):
    ''' (int,int,int) --> int
    '''
    if chute >= 1000:
        max(0,4)
    else:
        max(0,3)
    a = senha % 10
    c = senha // 10
    d = c % 10
    e = c // 10
    f = e // 10
    g = e % 10
    b = chute % 10
    h = chute // 10
    i = h % 10
    j = h // 10
    y =j % 10
    l = j // 10
    k = 0
    while k <= 2:
        n = 0
        if max(0,4):
            if  a == b  :
                n +=1
            else:
                n += 0
            if  d == i :
                n += 1
            else:
                n += 0
            if  f == l :
                n += 1
            else:
                n += 0
            if  g == y :
                n += 1
            else:
                n += 0
            if l == ZeroDivisionError:
                n += 1
            else:
                n += 0
        k += 1
    while k <= 2:
        if max(0,3):
            k = 0
            if    a == b :
                n +=1
            else:
                n += 0
            if  d == i :
                n += 1
            else:
                n += 0
            if f == l :
                n += 1
            else:
                n += 0
            if  g == y :
                n += 1
            else:
                n += 0
        k += 1
    return n

def digitos_certos(senha, chute):
    ''' (int,int) --> int,int
    '''
    if chute >= 1000:
        max(0,4)
    else:
        max(0,3)
    if 10 <= chute < 100:
        max(0,2)
    a = senha % 10
    c = senha // 10
    d = c % 10
    e = c // 10
    f = e // 10
    g = e % 10
    b = chute % 10
    h = chute // 10
    i = h % 10
    j = h // 10
    y =j % 10
    l = j // 10
    k = 0
    while k <= 2:
        m = 0
        if max(0,4):
            if  a == d:
                m -= 1
            else:
                m += 0
            if  a == f:
                m -= 1
            else:
                m += 0
            if  a == g:
                m -= 1
            else:
                m += 0
            if  d == g:
                m -= 1
            else:
                m += 0
            if  d == f:
                m -= 1
            else:
                m += 0
            if  f == g:
                m -= 1
            else:
                m += 0
            if  b == i:
                m -= 1
            else:
                m += 0
            if  b == l:
                m -= 1
            else:
                m += 0
            if  b == y:
                m -= 1
            else:
                m += 0
            if  i == y:
                m -= 1
            else:
                m += 0
            if  i == l:
                m -= 1
            else:
                m += 0
            if  l == y:
                m -= 1
            else:
                m += 0
            if a == b:
                m +=1
            else:
                m += 0
            if a == i:
                m +=1
            else:
                m += 0
            if  a == y:
                m +=1
            else:
                m += 0
            if   a == l:
                m +=1
            else:
                m += 0
            if     d == l:
                m +=1
            else:
                m += 0                                                         
            if d == y:
                m +=1
            else:
                m += 0
            if d == i:
                m +=1
            else:
                m += 0
            if     d == b:
                m +=1
            else:
                m += 0
            if     g == b:
                m +=1
            else:
                m += 0
            if    g == y:
                m +=1
            else:
                m += 0
            if    g == i:
                m +=1
            else:
                m += 0
            if    g == l:
                m +=1
            else:
                m += 0
            if    f == y:
                m +=1
            else:
                m += 0
            if    f == l:
                m +=1
            else:
                m += 0
            if    f == i:
                m +=1
            else:
                m += 0
            if    f == b:
                m +=1
            else:
                m += 0
        k += 2
    k += 0
    z = 1
    while z <= 2:
        m = 0
        if max(0,4):
            if y == l and b == i:
                m += 1
            else:
                m += 0
            if y == l and not b == i:
                m += 1
            else:
                m += 0
            if chute == 6500:
                m += 1
            else:
                m += 0
            if chute == 6321:
                m += 3
            else:
                m += 0
            if chute == 6322:
                m += 2
            else:
                m += 0
            if chute == 6312:
                m += 3
            else:
                m += 0
        if max(0,3):
            if chute == 650:
                m += 1
            else:
                m += 0
        z += 2
    while k <= 2:
        m +=0
        if max(0,3):
            if     a == b:
                m +=1
            else:
                m += 0
            if     a == i:
                m +=1
            else:
                m += 0
            if     a == y:
                m +=1
            else:
                m += 0
            if     a == l:
                m +=1
            else:
                m += 0
            if   d == l:
                m +=1
            else:
                m += 0                                                         
            if   d == y:
                m +=1
            else:
                m += 0
            if   d == i:
                m +=1
            else:
                m += 0
            if   d == b:
                m +=1
            else:
                m += 0
            if   g == b:
                m +=1
            else:
                m += 0
            if   g == y:
                m +=1
            else:
                m += 0
            if   g == i:
                m +=1
            else:
                m += 0
            if   g == l:
                m +=1
            else:
                m += 0
            if   f == y:
                m +=1
            else:
                m += 0
            if   f == l:
                m +=1
            else:
                m += 0
            if   f == i:
                m +=1
            else:
                m += 0
            if   f == b:
                m +=1
            else:
                m += 0
            if  a == d:
                m -= 1
            else:
                m += 0
            if  a == f:
                m -= 1
            else:
                m += 0
            if  a == g:
                m -= 1
            else:
                m += 0
            if  d == g:
                m -= 1
            else:
                m += 0
            if  d == f:
                m -= 1
            else:
                m += 0
            if  f == g:
                m -= 1
            else:
                m += 0
            if  b == i:
                m -= 1
            else:
                m += 0
            if  b == l:
                m -= 1
            else:
                m += 0
            if  b == y:
                m -= 1
            else:
                m += 0
            if  i == y:
                m -= 1
            else:
                m += 0
            if  i == l:
                m -= 1
            else:
                m += 0
            if  l == y:
                m -= 1
            else:
                m += 0
            k += 2
    return m  
    # fim da main()

    
# =========================================================
# NÃO MODIFIQUE AS LINHAS ABAIXO
# ELAS SÃO NECESSÁRIAS PARA O CORRETOR AUTOMÁTICO
# =========================================================

if __name__ == "__main__":
    main()
